from itertools import permutations
from models.InputStore import InputStore
from models.Timer import Timer


class Driver:
    def __init__(self, origin, destination, stops, method, choice):
        self.input_store = InputStore(origin, destination, stops, method, choice)
        self.time = Timer()
        self.build()

    def build(self):
        len_store = len(self.input_store.as_list())
        all = permutations(self.input_store.as_list())

        for path in all:
            if path[0] != self.input_store.origin or path[-1] != self.input_store.destination:
                continue
            print(path)
        
    def __str__(self):
        return self.input_store.__str__()
