class InputStore:
    def __init__(
        self, origin: str, destination: str, stops: list[str], method: str, choice: str
    ):
        self.origin = origin
        self.destination = destination
        self.stops = stops
        self.method = method
        self.choice = choice

    def as_list(self) -> list:
        return [self.origin] + self.stops + [self.destination]

    def __str__(self) -> str:
        return "Origin: {}\nDestination: {}\nStops: {}\nMethod: {}\nChoice: {}".format(
            self.origin, self.destination, self.stops, self.method, self.choice
        )
