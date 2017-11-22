import random
import string


# For all of the following functions, "ordering" signifies a dictionary mapping
# wizard names to their relative positions
# Example: ["Paul", "Katya", "Mudit"] is {"Paul": 1, "Katya": 2, "Mudit": 3}

# convert an ordering to a list
def dict_to_list(ordering):
    result = [""] * len(ordering)
    for wizard in ordering.keys():
        result[ordering[wizard] - 1] = wizard
    return result


# converts a list to an ordering
def lst_to_ordering(lst):
    return {lst[i]: i + 1 for i in range(len(lst))}


# return an ordering with the two wizards swapped
def swap(ordering, wizard, other_wizard):
    ordering = ordering.copy()
    ordering[wizard], ordering[other_wizard] = ordering[other_wizard], ordering[wizard]
    return ordering


# Given a particular ordering (dictionary from wizard names to positions) and set of constraints,
# Return (1) how many constraints were passed, (2) which ones were failed,
# (3) the wizard that violated the most constraints
def constraint_satisfaction(ordering, constraints):
    total_passed = 0
    constraint_violations = {key: 0 for key in ordering}
    for c in constraints:
        if ordering[c[2]] > ordering[c[1]] or ordering[c[2]] < ordering[c[0]]:
            total_passed += 1
        else:
            constraint_violations[c[0]] += 1;
            constraint_violations[c[1]] += 1;
            constraint_violations[c[2]] += 1
    return total_passed, constraint_violations, max(constraint_violations, key=lambda x: constraint_violations[x])


# which wizard is farther from the middle?
def farther(ordering, wizard1, wizard2):
    l = len(ordering)
    offset = 0
    if l % 2 == 0:
        offset = 0.5
    dist_to_middle_1 = abs(ordering[wizard1] - (l / 2 + offset))
    dist_to_middle_2 = abs(ordering[wizard2] - (l / 2 + offset))
    # print(dist_to_middle_1, dist_to_middle_2)
    if dist_to_middle_1 >= dist_to_middle_2:
        return wizard1
    return wizard2


# randomly generate a n-length list of length 10 alphanumeric wizard names
def random_list(n):
    lst = [''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) for i in range(n)]
    random.shuffle(lst)
    return lst
