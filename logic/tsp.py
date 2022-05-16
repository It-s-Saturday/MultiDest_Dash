from sys import maxsize as infinity
from itertools import permutations
from contextlib import suppress


def tsp(graph: dict[dict], origin, destination, choice):
    print("Start TSP")
    out_path = []
    evaluate = []
    for permutation in permutations(graph):  # permutations(graph) returns a list of all combinations of the
                                                    # routes
                                                 # i.e. input: [a, b, c]
                                                 # permutations = [[a,b,c], [a,c,b], [b,a,c], [b,c,a], [c,a,b], [c,b,a]]
        if permutation[0] == destination:
            break
        if permutation[0] != origin or permutation[-1] != destination:  # ignore permutations where our origin and
            #print("Bad hair day!")                                      # destination are not
                                                                        # where they're supposed to be
            continue
       # print(permutation)
        evaluate.append(permutation)  # construct a list of permutations to evaulate
    cost = infinity  # set cost equal to max value
    # print("evaluate set as", str(evaluate))
    c_calc = 0
    for path in evaluate:  # for each path in evaluate,
        # i = 0  # initialize iterator for this path
        c = 0  # initialize current cost
        for i in range(0, len(path)-1):  # iterate over path from first element to the last, excluding the last (see line 24)
                                    # i.e. ignore a -> c since they can't go direct from origin to dest
            with suppress(KeyError):  # ignores KeyErrors created when we skipped over duplicates on line 12
                # print("Calculated")
                temp_c = graph[path[i]][path[i + 1]]    # grabs the maps.py calculated value associated with the current
                                                        # position and the next position
                c += temp_c     # add onto the growing cost of the current path
                if c > cost:    #  ignore rest of path if intermediate cost is already greater
                    break       #  James Tiu
            # i += 1  # increment i (see line 21)
            c_calc += 1
        if cost != min(cost, c):  # if the cost != to the expression, it means it must be lower
            cost = min(cost, c)  # update new lowest cost
            out_path = path  # set out_path to this lowest cost path
            # print("cost set to {} | path set to {}".format(cost, out_path))
            print("New Min: {}".format(cost))
    print(c_calc, "routes calculated")
    # TODO: return the output as a string to computefromdjango.py
    # return list with first element as path and second element as metric
    out_metric = ""
    if choice == "distance":
        cost = round(cost, 2)
        out_metric = str(cost) + " mi"
    elif choice == "duration":
        out_hour = ""
        out_min = ""
        if cost >= 60:
            hours_cost = cost // 60
            mins_cost = cost % 60
            if hours_cost == 1:
                out_hour = "hour"
            else:
                out_hour = "hours"
            if mins_cost == 1:
                out_min = "min"
            else:
                out_min = "mins"

            out_metric = str(hours_cost) + " {} and ".format(out_hour) + str(mins_cost) + " {}".format(out_min)
        else:
            out_metric = str(cost) + " mins"

    return [out_path, out_metric]