import time


class Timer:
    def __init__(self, name):
        self.name = name
        self.start = time.time()

    def current_time(self):
        return time.time() - self.start

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Operation {} took {} seconds".format(self.name, self.current_time()))
