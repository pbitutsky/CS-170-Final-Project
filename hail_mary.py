
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

class GraphNode:


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


