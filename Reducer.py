
import util
import pycosat

# TODO Make Reducer into an object
# TODO Prune constraints
all_wizards = set()
all_positions = []  # make this a set!
all_variables = set()
cnf_set = set()
cnf_map = {}
cnf = []

#if two int arrays are permutations of each other
def is_permutation(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    mul = lambda x, y: x * y
    if reduce(mul, [x for x in lst1]) != reduce(mul, [x for x in lst2]):
        return False
    histogram = {}
    for item in lst1:
        if item not in histogram:
            histogram[item] = 1
        else:
            histogram[item] += 1
    for item in lst2:
        if item not in histogram:
            return False
        else:
            histogram[item] -= 1
    return sum(histogram.values()) == 0

def add_to_cnf(clause):
    mul = lambda x, y: x * y
    multiplied = reduce(mul, clause)
    if multiplied not in cnf_map:
        cnf_map[multiplied] = [clause]
    else:
        for x in cnf_map[multiplied]:
            if is_permutation(x, clause):
                return
        cnf_map[multiplied].append(clause)

    cnf.append(clause)

    # if str(clause) not in cnf_set:
        # cnf_set.add(str(clause))
        # cnf.append(clause)

class Wizard:
    def __init__(self, name):
        self.name = name
        self.variables = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Position:
    def __init__(self, number):
        self.number = number
        self.variables = []

    def __repr__(self):
        return str(self.number)

    def __str__(self):
        return str(self.number)

class Variable:
    def __init__(self, number, wizard, position):
        self.number = number
        self.wizard = wizard
        self.position = position

    def __str__(self):
        return str(self.wizard) + str(self.position)

    def __repr__(self):
        return str(self.wizard) + str(self.position)



#Given a list of constraints, and set of wizards, reduce the problem to an expression in CNF
def reduce_to_SAT(constraints, wizards):
    # variables = [i for i in range(1, len(wizards)**2+1)] #there are n^2 variables
    # english_variables = [wizards[(i-1)%n] + str(((i-1)//n)+1) for i in range(1, len(wizards)**2+1)]
    # print(variables)
    # print(english_variables)
    n = len(wizards)
    for i in range(1, n**2+1):
        wizard_name = wizards[(i-1)%n]
        # print(wizard_name)

        # create a new Wizard
        wiz = Wizard(wizard_name)

        # don't use that wizard if the wizard is already in the set
        for wizard in all_wizards:
            if wizard.name == wizard_name:
                wiz = wizard

        # if the wizard is not in the set, add him
        if wiz not in all_wizards: all_wizards.add(wiz)

        # create a new Position if i < num_wizards
        # else find it in the list of positions
        pos_as_int = ((i-1)//n)+1
        pos = Position(pos_as_int)
        for position in all_positions:
            if pos_as_int == position.number:
                pos = position
        if pos not in all_positions: all_positions.append(pos) # TODO: change to add and make it a set

        assert pos # make sure we have a position

        #create a new Variable
        variable = Variable(i, wiz, pos)
        all_variables.add(variable)

        # print(wiz, pos, variable, pos_as_int)

        # associate that Variable with it's wizard and position
        wiz.variables.append(variable)
        pos.variables.append(variable)


    initialization()
    constraints_to_cnf(constraints)
    return cnf

def initialization():

    for pos in all_positions:
        vars = pos.variables
        for i in range(len(vars)):
            for j in range(i + 1, len(vars)):
                english = "If " + str(vars[i]) + " then not " + str(vars[j]) + "."
                clause = [-vars[i].number, -vars[j].number]
                # print(english, clause)
                add_to_cnf(clause)
    # print("\n")
    for wiz in all_wizards:
        vars = wiz.variables
        for i in range(len(vars)):
            for j in range(i + 1, len(vars)):
                english = "If " + str(vars[i]) + " then not " + str(vars[j]) + "."
                clause = [-vars[i].number, -vars[j].number]
                # print(english, clause)
                add_to_cnf(clause)

    for pos in all_positions:
        vars = pos.variables
        english = []
        clause = []
        for v in vars:
            english.append(str(v))
            clause.append(v.number)
        # print(" and ".join(english), clause)
        add_to_cnf(clause)

    for wiz in all_wizards:
        vars = wiz.variables
        english = []
        clause = []
        for v in vars:
            english.append(str(v))
            clause.append(v.number)
        # print(" and ".join(english), clause)
        add_to_cnf(clause)

#given a string wizard, returns the object
def find_wizard(wizard_name):
    for wizard in all_wizards:
        if wizard.name == wizard_name:
            return wizard
    raise Exception("Unable to locate wizard " + wizard_name, all_wizards)

def find_variable(variable_number):
    for var in all_variables:
        if var.number == variable_number:
            return var


def constraints_to_cnf(constraints):
    for constraint in constraints:
        w1, w2, w3 = [find_wizard(w) for w in constraint]
        for i in w1.variables:
            w1_pos = i.position
            for j in w2.variables:
                w2_pos = j.position
                if w1_pos.number == w2_pos.number:
                    continue
                for k in w3.variables:
                    w3_pos = k.position
                    if w3_pos.number == w1_pos.number or w3_pos.number == w2_pos.number:
                        continue
                    allowed = w3_pos.number not in range(w1_pos.number, w2_pos.number) \
                              and w3_pos.number not in range(w2_pos.number, w1_pos.number)
                    # print(i, j, k, w1_pos, w2_pos, w3_pos, allowed)
                    if not allowed:
                        add_to_cnf([-i.number, -j.number, -k.number])


def solve(constraints, num_wizards):
    # annoying hack but I needed this for generate_output_files.py
    global all_wizards, all_positions, all_variables, cnf_set, cnf
    all_wizards = set()
    all_positions = []  # make this a set!
    all_variables = set()
    cnf_set = set()
    cnf = []
    wizards = sorted(util.get_wizards_from_constraints(constraints))
    # print(wizards)
    assert len(wizards) == num_wizards
    # constraints = prune(constraints)
    print("Reducing")
    cnf = reduce_to_SAT(constraints, wizards)
    # for clause in cnf:
    #     print(clause)
    print("Clauses: ", len(cnf))
    print("Evaluating")
    pycosat_result = pycosat.solve(cnf)
    # print(pycosat_result)

    result = ["" for x in range(len(wizards))]
    for var_num in pycosat_result:
        if var_num > 0:
            var = find_variable(var_num)
            wizard, position = var.wizard, var.position
            result[position.number-1] = wizard.name
    return result


    #pycosat logic here

# constraints = [['a', 'b', 'c'], ['d', 'c', 'b']]
# solve(constraints)

