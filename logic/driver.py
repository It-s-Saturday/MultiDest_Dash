from itertools import permutations

from models.InputStore import InputStore

from models.Timer import Timer

from models.GoogleApi import GoogleApi


class Driver:
    def __init__(self, origin, destination, stops, method, choice):
        self.input_store = InputStore(origin, destination, stops, method, choice)
        self.already_looked_up = {}
        self.time = Timer()
        # self.GoogleApi = GoogleApi()
        self.build_valid_paths()
        # self.build_adj_matrix()

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
        adj_matrix = {}
        for i_origin in self.input_store.as_list():
            for i_dest in self.input_store.as_list():
                if i_origin == i_dest:
                    continue
                adj_matrix[i_origin][i_dest] = self.lookup(i_origin, i_dest)

        print(adj_matrix)

    def lookup(self, a, b):
        to_lookup = []
        if a not in self.already_looked_up:
            to_lookup.append(a)

        if b not in self.already_looked_up:
            to_lookup.append(b)

        if to_lookup:
            for place in to_lookup:
                self.already_looked_up[place] = self.namelookup(
                    place, self.input_store.method, self.input_store.choice
                )

        return self.GoogleApi.lookup(
            self.already_looked_up[a],
            self.already_looked_up[b],
            self.input_store.method,
            self.input_store.choice,
        )

    def namelookup(self, search, method="driving", choice="distance"):
        """Uses the GoogleMaps API to retrieve a JSON that contains the searched name, then use this for lookup)"""
        origin = search.replace(" ", "+")
        destination = search.replace(" ", "+")
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
        concat = (
            url
            + "origins="
            + origin
            + "&destinations="
            + destination
            + "&key="
            + api_key
            + "&mode="
            + mode
        )
        concat = f"{url}origins={origin}&destinations={destination}&key={api_key}&mode={mode}"
        r = requests.get(concat)
        name = r.json()["destination_addresses"][0]
        return name

    def __str__(self):
        return self.input_store.__str__()
