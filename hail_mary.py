
import argparse

variable_map = {}
SAT_clauses = []

# PAUL
def generate_variables(wizards):
    pass

# PAUL
def generate_constraint_clauses(constraints):
    pass

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
    generate_variables(wizards)
    generate_constraint_clauses(constraints)
    generate_transitivity_clauses(wizards)
    
    true_variables = solve_SAT(SAT_clauses)
    graph = generate_var_relationship_graph(true_variables)
    result = find_ordering(graph)
    return result

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)
                
    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    args = parser.parse_args()
    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)

    # TEST HERE
    print(wizards)






