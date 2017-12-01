from util import *

class OlsSolver:

    def __init__(self):
        pass

    def solve(self, lst, constraints):

        current_constraint = 0
        constraints_met = 0
        ordering = {lst[i]: i + 1 for i in range(len(lst))}

        visited = set()
        path = []
        counter = 0
        good_example = False
        iterations = 0
        while constraints_met <= len(constraints):
            # print(ordering)
            # check if a constraint is met
            wizard1, wizard2, wizard3 = constraints[current_constraint]
            if (ordering[wizard2] > ordering[wizard3] > ordering[wizard1]) or (
                            ordering[wizard1] > ordering[wizard3] > ordering[wizard2]):
                # constraint not met
                # print("FAILED: ", wizard1, wizard2, wizard3)
                farther_wizard = farther(ordering, wizard1, wizard2)
                new_ordering = swap(ordering, farther_wizard, wizard3)
                # print(visited)
                # make sure we haven't visited this ordering before
                if str(new_ordering) in visited:
                    if farther_wizard == wizard1:
                        new_ordering = swap(ordering, wizard2, wizard3)
                        path.append((wizard2, wizard3))
                    else:  # wizard2 is farther
                        new_ordering = swap(ordering, wizard1, wizard3)
                        path.append((wizard1, wizard3))
                else:
                    path.append((farther_wizard, wizard3))

                if str(new_ordering) in visited:
                    # print("BACKTRACK")
                    last_swap = path.pop()
                    new_ordering = swap(ordering, last_swap[0], last_swap[1])
                    good_example = True
                    counter += 1

                    # try random

                ordering = new_ordering
                visited.add(str(new_ordering))

                # print(dict_to_list(ordering))
            else:
                # constraint met
                # print(constraints_met, "Passed: ", wizard1, wizard2, wizard3)
                constraints_met += 1

            # avoid infinite loop by setting constraints_met back to 0
            if constraints_met == len(constraints):
                break

            if current_constraint >= len(constraints) - 1:
                current_constraint = 0
                constraints_met = 0
                iterations += 1
            else:
                current_constraint += 1

        #return good_example, counter, iterations, dict_to_list(ordering)
        return ordering
