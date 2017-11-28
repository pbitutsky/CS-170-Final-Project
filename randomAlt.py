import random
import util
import Solver
def random_check(constraints, start_ordering):
    print("HAPPENONG");
    ordering = start_ordering
    print(ordering)
    total_passed, violations, max_violator = \
        util.constraint_satisfaction(ordering, constraints)
    minimum = float('inf')
    counter = 0
    while total_passed != len(constraints):
        ordering_as_list = util.dict_to_list(ordering)
        print(total_passed, minimum, max_violator, ordering_as_list)
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
            print("SOLVING NOW", minimum)
            s = Solver.Solver()
            s.solve(util.dict_to_list(min_violations), constraints)

    return ordering



