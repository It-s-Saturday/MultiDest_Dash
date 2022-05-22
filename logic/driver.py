from itertools import permutations

from models.GoogleApi import GoogleApi
from models.InputStore import InputStore
from models.Timer import Timer
from logic.helpers import debug


class Driver:
    def __init__(self, origin, destination, stops, method, choice):
        self.input_store = InputStore(origin, destination, stops, method, choice)
        self.already_looked_up = {}
        self.GoogleApi = GoogleApi()
        self.build_valid_paths()
        self.adj_matrix = {}
        self.build_adj_matrix()
        

    def build_valid_paths(self):
        len_store = len(self.input_store.as_list())
        intermediates = permutations(self.input_store.as_list()[1:-1])
        out = [x for x in intermediates]
        valid_paths = []
        for permutation in out:
            valid_paths += [
                [self.input_store.origin]
                + list(permutation)
                + [self.input_store.destination]
            ]
        print(f"created:\n{valid_paths}")
        return valid_paths

    def build_adj_matrix(self):
        with Timer('build matrix') as matrix_timer:
            for i_origin in self.input_store.as_list():
                for i_dest in self.input_store.as_list():

                    if i_origin == i_dest:
                        continue
                    lookup = self.lookup(i_origin, i_dest)
                    converted_origin = self.already_looked_up[i_origin]
                    converted_dest = self.already_looked_up[i_dest]
                    if converted_origin not in self.adj_matrix:
                        self.adj_matrix[converted_origin] = {converted_dest: lookup}
                    else:
                        self.adj_matrix[converted_origin][converted_dest] = lookup
            debug('matrix', self.adj_matrix)

    def lookup(self, a, b):
        to_lookup = []
        if a not in self.already_looked_up:
            to_lookup.append(a)

        if b not in self.already_looked_up:
            to_lookup.append(b)

        if to_lookup:
            for place in to_lookup:
                print(f"looking up {place}")
                self.already_looked_up[place] = self.GoogleApi.namelookup(
                    place, self.input_store.method, self.input_store.choice
                )
                print(self.already_looked_up[place])
        debug(
            "stores",
            f"{a}: {self.already_looked_up[a]}",
            f"{b}: {self.already_looked_up[b]}",
        )
        return self.GoogleApi.lookup(
            self.already_looked_up[a],
            self.already_looked_up[b],
            self.input_store.method,
            self.input_store.choice,
        )

    def __str__(self):
        return self.input_store.__str__()
