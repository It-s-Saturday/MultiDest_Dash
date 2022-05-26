import math

class Calculator:
    def __init__(self, adj_matrix=None, input_store=None):
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
                    # not worth to continue calculating 
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
            if i % 2: continue
            next = lst[i+1].strip(',') if i+1 < len(lst) else None
            if next and is_digit(element):
                if 'day' in next:
                    time += int(element) * 1440
                elif 'hour' in next:
                    time += int(element) * 60
                elif 'min' in next:
                    time += int(element)
        return time

if __name__ == '__main__':
    c = Calculator()
    assert(c.parse_time("1 day, 1 hour, 1 min") == 1501)
    assert(c.parse_time("2 days, 2 hours, 2 mins") == 3002)
    assert(c.parse_time("1 day, 3 hours") == 1620)
    print("All tests passed")