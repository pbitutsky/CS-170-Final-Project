
variable_to_wizards = {}
wizards_to_variable = {}
SAT_clauses = []

def get_sorted_wizard_tuple(wiz_tuple):
    if wiz_tuple[0] > wiz_tuple[1]:
        return (wiz_tuple[1], wiz_tuple[0])
    return (wiz_tuple[0], wiz_tuple[1])


# PAUL
def generate_variables_and_constraint_clauses(wizards, constraints):
    counter = 1
    for constraint in constraints:
        w1, w2, w3 = constraint

        wizard_tuple1 = (w1, w3)
        wizard_tuple2 = (w2, w3)

        #generate the variables
        for wiz_tuple in [wizard_tuple1, wizard_tuple2]:

            #create a sorted wiz tuple
            sorted_wiz_tuple = get_sorted_wizard_tuple(wiz_tuple)
            if sorted_wiz_tuple not in wizards_to_variable:
                if counter not in variable_to_wizards:
                    wizards_to_variable[sorted_wiz_tuple] = counter
                    variable_to_wizards[counter] = sorted_wiz_tuple
                    counter += 1
                else:
                    raise Exception("This shouldn't happen")

        print(variable_to_wizards)
        a = wizards_to_variable[get_sorted_wizard_tuple(wizard_tuple1)]
        b = wizards_to_variable[get_sorted_wizard_tuple(wizard_tuple2)]

        clauses = [[-a, b], [a, -b]]
        SAT_clauses.extend(clauses)

# KATYA
def generate_transitivity_clauses(wizards):
    pass

# class GraphNode:


def generate_var_relationship_graph(true_variables):
    pass

# input is the SAT clauses, output is true_variables
def solve_SAT():
    pass

# run topological sort on graph, returns wizard ordering 
def find_ordering(graph):
    pass

def solve(wizards, constraints):
    generate_variables_and_constraint_clauses(wizards, constraints)
    generate_transitivity_clauses(wizards)

    true_variables = solve_SAT(SAT_clauses)
    graph = generate_var_relationship_graph(true_variables)
    result = find_ordering(graph)
    return result


# generate_variables_and_constraint_clauses(['a', 'b', 'c', 'd'], [['a', 'b', 'c'], ['a', 'c', 'd'], ['b', 'c', 'a']])
# print(variable_to_wizards)
# print(wizards_to_variable)
# print(SAT_clauses)