from models.InputStore import InputStore
from models.Timer import Timer


class Driver:
    def __init__(self, origin, destination, stops, method, choice):
        self.input_store = InputStore(origin, destination, stops, method, choice)
        self.time = Timer()
        self.build()

    def build(self):
        len_store = len(self.input_store.as_list())
        iterable = enumerate(self.input_store.as_list())
        for i, this_location in iterable:
            for j, other_location in iterable:
                if (
                    (i == j)
                    or (i == 0 and j == len_store - 1)
                    or (i == len_store - 1 and j == 0)
                ):
                    continue
                print(this_location, other_location)

    def __str__(self):
        return self.input_store.__str__()
