import math
from logic.helpers import debug


def naive_tsp(valid_paths, adj_matrix, already_looked_up):
    out_path = []
    out_cost = math.inf

    for path in valid_paths:
        temp_cost = 0
        # debug("Current path", path)

        for i, stop in enumerate(path[:-1]):
            next_stop = path[i + 1] if i <= len(path) else None
            if stop not in already_looked_up:
                raise Exception("Unhandled stop exception")

            lookup = lambda start, end: adj_matrix[already_looked_up[start]][
                already_looked_up[end]
            ]

            between = lookup(stop, next_stop)
            # debug("Current stop", stop, "next stop", next_stop, "between", between)


            temp_cost += between
            
            if temp_cost > out_cost:  # temp cost exceeds out_cost prematurely
                # debug("exceeded...going next")
                break
            

        if temp_cost < out_cost and i >= len(path) - 2:
            debug("Updating cost", out_cost, "to", temp_cost)
            out_path = path
            out_cost = temp_cost

    return [out_path, out_cost]

def is_digit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def parse_time(str):
    """Return minutes version from string containing days, hours, minutes"""
    lst = str.split(" ")
    time = 0
    
    if "mi" in str:
        return parse_distance(str)

    for i, element in enumerate(lst):
        if i % 2:
            continue
        next = lst[i + 1].strip(",") if i + 1 < len(lst) else None
        if next and is_digit(element):
            if "day" in next:
                time += int(element) * 1440
            elif "hour" in next:
                time += int(element) * 60
            elif "min" in next:
                time += int(element)
    return time

def parse_distance(str):
    """Return float of miles from string containing distance and units"""
    return float(str.split()[0])

if __name__ == "__main__":
    assert parse_time("1 day, 1 hour, 1 min") == 1501
    assert parse_time("2 days, 2 hours, 2 mins") == 3002
    assert parse_time("1 day, 3 hours") == 1620
    # debug("All tests passed")
