import math

class Calculator:
    def __init__(self, adj_matrix, input_store):
        self.adj_matrix = adj_matrix
        self.input_store = input_store
    
    def get_min_path(self):
        min = math.inf
        min_path = []
        
        accumulator = 0

        for origin in self.adj_matrix:
            temp_path = [origin]
            for stop in self.adj_matrix[origin]:
                if stop == origin:
                    continue
                distance_between = self.adj_matrix[origin][stop]
                metric = self.parse_time(distance_between)
                accumulator += metric
                if accumulator > min and len(temp_path) < len(self.input_store.as_list()):
                    break
                temp_path.append(stop)

    def parse_time(self, str):
        """Return minutes version from string containing days, hours, minutes"""
        lst = str.split(" ")
        time = 0

        def is_digit(value):
            try:
                int(value)
                return True
            except ValueError:
                return False

        for i, element in enumerate(lst):
            next = lst[i+1] if i+1 < len(lst) else None
            if next and is_digit(next):
                if 'day' in next:
                    time += int(element) * 1440
                elif 'hour' in next:
                    time += int(element) * 60
                elif 'min' in next:
                    time += int(element)
        return time