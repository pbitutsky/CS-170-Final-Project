import random
import util
<<<<<<< HEAD
import Solver

import output_validator

def random_check(constraints, start_ordering):
    print("STARTING")
    ordering = start_ordering
    maximum = float('-inf')
    constraints_satisfied = 0
    while constraints_satisfied != len(constraints):
        random.shuffle(ordering)
        if constraints_satisfied > maximum:
            maximum = constraints_satisfied
            max_violations = ordering
            print("New Max: ", maximum, max_violations)
        constraints_satisfied = validate_constraints(constraints, ordering)
=======
import OldSolver
def random_check(constraints, start_ordering):
    print("HAPPENING");
    ordering = start_ordering
    total_passed, violations, max_violator = \
        util.constraint_satisfaction(ordering, constraints)
    minimum = float('inf')
    counter = 0
    while total_passed != len(constraints):
        ordering_as_list = util.dict_to_list(ordering)
        # print(total_passed, minimum, max_violator, ordering_as_list)
        random.shuffle(ordering_as_list)
        ordering = util.lst_to_ordering(ordering_as_list)
        if total_passed < minimum:
            minimum = total_passed
            min_violations = ordering
            counter = 0
        total_passed, violations, max_violator = \
            util.constraint_satisfaction(ordering, constraints)
        counter += 1
        if counter > 10000:
            print(counter)
            print(len(violations))
            return ordering
    print('violations: ' + violations)
>>>>>>> a41effa322c0124f2fcb4f57c88649aba6bd4c82
    return ordering

def validate_constraints(constraints, output_ordering):
    constraints_satisfied = 0
    constraints_failed = []
    for constraint in constraints:
        c = constraint  # Creating an alias for easy reference
        m = {k: v for v, k in enumerate(output_ordering)}  # Creating an alias for easy reference

        wiz_a = m[c[0]]
        wiz_b = m[c[1]]
        wiz_mid = m[c[2]]

        if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
            constraints_failed.append(c)
        else:
            constraints_satisfied += 1

<<<<<<< HEAD
    return constraints_satisfied
=======


>>>>>>> a41effa322c0124f2fcb4f57c88649aba6bd4c82
