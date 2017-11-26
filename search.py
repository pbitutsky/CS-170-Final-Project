import Queue as Q

"""
To consider: how to avoid expanding subproblems we've already seen before

Less slicing, more bitstrings
"""


def search(constraints, total_wizards):
    # initial subproblem: tuple of the list of unsatisfied constraints and the ordering so far
    initial = (constraints, [])
    # S: set of active subproblems
    S = Q.PriorityQueue()
    visited = set()
    S.put(initial, len(constraints))  # Why is the length of the unsatisfied constraints the priority?
    visited.add(str(initial))
    while not S.empty():
        current = S.get()
        print(str(current[1]) + '\n')
        new_subproblems = expand(current)
        for p in new_subproblems:
            # if the test succeeds, return the list in this subproblem as the solution
            if test(p, total_wizards) == 1:
                return p[1]
            # if test doesn't fail, add subproblem to PQ
            elif test(p, total_wizards) != -1 and str(p) not in visited:
                visited.add(str(p))
                S.put(p, len(p[0]))
            # if the test fails, don't add the subproblem to the PQ
    # didn't find a solution
    return None


# test if a subproblem satisfies all constraints and if all wizards in ordering
def test(subprob, total_wizards):
    constraints = subprob[0]
    ordering = subprob[1]
    num_wizards = len(ordering)
    num_constraints_satisfied = 0
    for c in constraints:
        if c[0] in ordering and c[1] in ordering and c[2] in ordering:
            wiz1_index = ordering.index(c[0])
            wiz2_index = ordering.index(c[1])
            wiz3_index = ordering.index(c[2])
            if wiz1_index < wiz3_index < wiz2_index or wiz1_index > wiz3_index > wiz2_index:
                return -1
            else:
                num_constraints_satisfied += 1
    if num_wizards == total_wizards:
        return 1
    else:
        return 0


def expand(subprob):
    # satisfy first unsatisfied constraint in list
    i = 0
    # copy old list of constraints
    new_constraints = subprob[0][:]
    c = subprob[0][i]
    ordering = subprob[1]
    while const_satisfied(ordering, c):
        del new_constraints[0]
        c = subprob[0][i]
        i += 1
    # delete the constraint we're about to satisfy in the new orderings
    del new_constraints[0]
    # all 3 wizards already in ordering, but they're violating the constraint. this case might never happen?!
    new_subproblems = []
    if c[0] in ordering and c[1] in ordering and c[2] in ordering:
        print("this case shouldn't happen")
    # 2 out of 3 wizards in ordering
    # first two in ordering
    elif c[0] in ordering and c[1] in ordering:
        new_wizard = c[2]
        wizA_index = ordering.index(c[0])
        wizB_index = ordering.index(c[1])
        new_subproblems = generate_placements_wiz3(new_constraints, ordering, wizA_index, wizB_index, c[2])
    # one of the first two in ordering, and the third one in ordering
    elif (c[1] in ordering and c[2] in ordering) or (c[0] in ordering and c[2] in ordering):
        if c[1] in ordering:
            wizB = c[0]
            wizA_index = ordering.index(c[1])
        elif c[0] in ordering:
            wizB = c[1]
            wizA_index = ordering.index(c[0])
        wiz3_index = ordering.index(c[2])
        new_subproblems = generate_placements_wizB(new_constraints, ordering, wizA_index, wizB, wiz3_index)
    # only wiz3 in odering
    elif c[2] in ordering:
        wiz3_index = ordering.index(c[2])
        wizA = c[0]
        wizB = c[1]
        new_subproblems = []
        i = 0
        while i <= len(ordering):
            new_order = ordering[:]
            new_order.insert(i, wizA)
            more_subproblems = generate_placements_wizB(new_constraints, new_order, i, wizB, wiz3_index)
            new_subproblems.extend(more_subproblems)
            i += 1
    # only one of the first two wizards in ordering
    elif c[0] in ordering or c[1] in ordering:
        if c[0] in ordering:
            wizA_index = ordering.index(c[0])
            wizB = c[1]
        if c[1] in ordering:
            wizA_index = ordering.index(c[1])
            wizB = c[0]
        wiz3 = c[2]
        new_subproblems = []
        i = 0
        while i <= len(ordering):
            new_order = ordering[:]
            new_order.insert(i, wizB)
            more_subproblems = generate_placements_wiz3(new_constraints, new_order, wizA_index, i, wiz3)
            new_subproblems.extend(more_subproblems)
            i += 1
    # no wizards in ordering- place first two anywhere, place third based on those
    else:
        wizA = c[0]
        wizB = c[1]
        wiz3 = c[2]
        i = 0
        for i in range(len(ordering) + 1):
            new_order = ordering[:]
            new_order.insert(i, wizA)
            for j in range(len(new_order) + 1):
                new_new_order = new_order[:]
                new_new_order.insert(j, wizB)
                wizA_index = new_new_order.index(wizA)
                more_subproblems = generate_placements_wiz3(new_constraints, new_new_order, wizA_index, j, wiz3)
                new_subproblems.extend(more_subproblems)
    return new_subproblems


# returns a list of new subproblems
def generate_placements_wiz3(constraints, ordering, wizA_index, wizB_index, wiz3):
    new_wizard = wiz3
    younger_wiz = min(wizA_index, wizB_index)
    older_wiz = max(wizA_index, wizB_index)
    new_subproblems = []
    # add new wizard in before younger wizard
    i = 0
    while i <= younger_wiz:
        new_order = ordering[:]
        new_order.insert(i, new_wizard)
        new_subproblems.append((constraints, new_order))
        i += 1
    # add new wizard in after older wizard
    i = older_wiz + 1
    while i <= len(ordering):
        new_order = ordering[:]
        new_order.insert(i, new_wizard)
        new_subproblems.append((constraints, new_order))
        i += 1
    return new_subproblems


# returns a list of new subproblems
def generate_placements_wizB(constraints, ordering, wizA_index, wizB, wiz3_index):
    new_subproblems = []
    new_wizard = wizB
    # print("finding wizB placement")
    if wiz3_index > wizA_index:
        # wizB can go anywhere before wiz3
        i = 0
        while i < wiz3_index:
            new_order = ordering[:]
            new_order.insert(i, new_wizard)
            new_subproblems.append((constraints, new_order))
            i += 1
    elif wizA_index > wiz3_index:
        # wizB can go anywhere after wiz3
        i = wiz3_index + 1
        while i <= len(ordering):
            new_order = ordering[:]
            new_order.insert(i, new_wizard)
            new_subproblems.append((constraints, new_order))
            i += 1
    return new_subproblems


# do these three wizards exisit in the current ordering and is the constraint satisfied
def const_satisfied(ordering, c):
    if c[0] in ordering and c[1] in ordering and c[2] in ordering:
        return (ordering.index(c[2]) < ordering.index(c[1]) and ordering.index(c[2]) < ordering.index(c[0])) \
               or (ordering.index(c[2]) > ordering.index(c[1]) and ordering.index(c[2]) > ordering.index(c[0]))
    else:
        return False


if __name__ == '__main__':
    main(sys.argv[1:])
