from itertools import permutations

from models.GoogleApi import GoogleApi
from models.InputStore import InputStore
from models.Timer import Timer
from logic.helpers import debug
from logic.calculator import naive_tsp, parse_time


class Driver:
    def __init__(self, origin, destination, stops, method="driving", metric="time"):
        with Timer("total runtime") as total_timer:
            self.input_store = InputStore(origin, destination, stops, method, metric)
            self.already_looked_up = {}
            self.GoogleApi = GoogleApi()
            self.valid_paths = self.build_valid_paths()
            self.adj_matrix = {}
            self.build_adj_matrix()
            self.tsp = self.naive_tsp()
            debug("tsp", self.tsp)
            self.best_path = self.tsp[0]
            debug("best path", self.best_path)
            self.cost = self.tsp[1]
            debug("cost", self.cost)
            self.parsed_best_path = self.parse_path()
            # debug("best path", self.best_path)

    def parse_path(self):
        out = []
        for position in self.best_path:
            out.append(self.already_looked_up[position])
        return out

    def naive_tsp(self):
        with Timer("naive tsp") as naive_timer:
            return naive_tsp(self.valid_paths, self.adj_matrix, self.already_looked_up)

    def build_valid_paths(self):
        intermediates = permutations(self.input_store.stops)
        out = [x for x in intermediates]
        valid_paths = []
        for permutation in out:
            valid_paths += [
                [self.input_store.origin]
                + list(permutation)
                + [self.input_store.destination]
            ]
        # debug(f"created:\n{valid_paths}")
        return valid_paths

    def build_adj_matrix(self):
        with Timer("build matrix") as matrix_timer:
            iterations = 0
            for i_origin in self.input_store.as_list()[:-1]:
                for i_dest in self.input_store.as_list()[1:]:
                    if i_origin == i_dest or (
                        i_origin == self.input_store.origin
                        and i_dest == self.input_store.destination
                    ):
                        continue
                    lookup = parse_time(self.lookup(i_origin, i_dest))
                    converted_origin = self.already_looked_up[i_origin]
                    converted_dest = self.already_looked_up[i_dest]
                    if converted_origin not in self.adj_matrix:
                        self.adj_matrix[converted_origin] = {converted_dest: lookup}
                    else:
                        self.adj_matrix[converted_origin][converted_dest] = lookup
                    iterations += 1

        # debug("matrix", self.adj_matrix, "iterations", iterations)

    def lookup(self, a, b):
        try:
            stored_a = self.already_looked_up[a]
            stored_b = self.already_looked_up[b]
            # debug("optimized", stored_a, stored_b, self.adj_matrix[stored_a][stored_b])
            return self.adj_matrix[stored_a][stored_b]

        except:
            to_lookup = []
            if a not in self.already_looked_up:
                to_lookup.append(a)

            if b not in self.already_looked_up:
                to_lookup.append(b)

            if to_lookup:
                for place in to_lookup:
                    # Key = user input, Value = Google API response
                    self.already_looked_up[place] = self.GoogleApi.namelookup(
                        place, self.input_store.method, self.input_store.choice
                    )
            # debug("google lookup", self.already_looked_up[a], self.already_looked_up[b])
            return self.GoogleApi.lookup(
                self.already_looked_up[a],
                self.already_looked_up[b],
                self.input_store.method,
                self.input_store.choice,
            )

    def __str__(self):
        return self.input_store.__str__()
