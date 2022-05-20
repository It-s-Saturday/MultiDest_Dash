from models.InputStore import InputStore
from models.Timer import Timer


class Driver:
    def __init__(self, origin, destination, stops, method, choice):
        self.input_store = InputStore(origin, destination, stops, method, choice)
        self.time = Timer()
        self.build()

    def __str__(self):
        return "Origin: {}\nDestination: {}\nStops: {}\nMethod: {}\nChoice: {}".format(
            self.origin, self.destination, self.stops, self.method, self.choice
        )

    def build(self):
        for location in self.input_store.as_list():
            print(location)
