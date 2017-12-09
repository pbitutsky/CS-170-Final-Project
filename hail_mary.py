import argparse
import string

from toposort import toposort, toposort_flatten
import pycosat
import random
import itertools

def get_reverse_tuple(wiz_tuple):
    return (wiz_tuple[1], wiz_tuple[0])

class HailMary:

    def __init__(self):
        self.variable_to_wizards = {}
        self.wizards_to_variable = {}
        self.SAT_clauses = []

    def prune_constraints(self, constraints):
        pruned = []
        for c in constraints:
            found = False
            for p in pruned:
                if c[2] == p[2] and ((c[0] == p[0] and c[1] == p[1]) or (c[0] == p[1] and c[1] == p[0])):
                    found = True
                    break
            if not found:
                pruned.append(c)
        return pruned

    def generate_variables(self, wizards):
        counter = 1
        for a in wizards:
            for b in wizards:
                if a != b:
                    tup = (a, b)
                    if tup not in self.wizards_to_variable:
                        if counter not in self.variable_to_wizards:
                            self.wizards_to_variable[tup] = counter
                            self.variable_to_wizards[counter] = tup
                        else:
                            raise Exception("THIS REALLY SHOULD NOT HAPPEN")
                    counter += 1

    def generate_additional_clauses(self):
        for tup in self.wizards_to_variable:

            reversed_tup = get_reverse_tuple(tup)
            if reversed_tup not in self.wizards_to_variable:
                raise Exception("VARIABLES NOT CORRECTLY INPUT")
            A = self.wizards_to_variable[tup]
            B = self.wizards_to_variable[reversed_tup]
            self.SAT_clauses.append([-A, -B])
            self.SAT_clauses.append([A, B])

    # PAUL
    def generate_constraint_clauses(self, wizards, constraints):
        counter = 1
        helper = lambda wizard_tuple: wizard_tuple[0] + " < " + wizard_tuple[1]
        for constraint in constraints:
            w1, w2, w3 = constraint

            wizard_tuple1 = (w1, w3)
            wizard_tuple2 = (w2, w3)
            # print(constraint)
            # print(wizard_tuple1, wizard_tuple2, get_reverse_tuple(wizard_tuple1), get_reverse_tuple(wizard_tuple2))

            #generate the variables
            for wiz_tuple in [wizard_tuple1, wizard_tuple2,
                              get_reverse_tuple(wizard_tuple1), get_reverse_tuple(wizard_tuple2)]:

                #create a sorted wiz tuple
                reverse_wiz_tuple = get_reverse_tuple(wiz_tuple)
                # if wiz_tuple not in self.wizards_to_variable:
                    # raise Exception("BUT I ADDED EVERYTHING")

            a = self.wizards_to_variable[wizard_tuple1]
            b = self.wizards_to_variable[wizard_tuple2]
            c = self.wizards_to_variable[get_reverse_tuple(wizard_tuple1)]
            d = self.wizards_to_variable[get_reverse_tuple(wizard_tuple2)]

            clauses = [[a, c], [a, d], [b, c], [b, d]]
            self.SAT_clauses.extend(clauses)

    # KATYA
    def generate_transitivity_clauses(self, wizards):
        for a in wizards:
            for b in wizards:
                for c in wizards:
                    if a != b and b != c and a != c: #(a < b and b < c and a < c):
                        var1 = self.wizards_to_variable[(a, b)]
                        var2 = self.wizards_to_variable[(b, c)]
                        var3 = self.wizards_to_variable[(a, c)]
                        self.SAT_clauses.append([-var1, -var2, var3])

    def find_ordering(self, wizards, SAT_result):
        graph = {}
        for w in wizards:
            graph[w] = set()
        for var in SAT_result:
            wiz1, wiz2 = self.variable_to_wizards[abs(var)]
            if var > 0:
                graph[wiz1].add(wiz2)
        return toposort_flatten(graph)

    # input is the SAT clauses, output is true_variables
    def solve_SAT(self):
        return pycosat.solve(self.SAT_clauses)

    def sanity_check(self, SAT_result):
        temp_map = {}
        for var in SAT_result:
            wiz_tuple = self.variable_to_wizards[abs(var)]
            if var > 0:
                print("Wizard " + wiz_tuple[0] + " should be before " + wiz_tuple[1])
                if wiz_tuple[0] not in temp_map:
                    temp_map[wiz_tuple[0]] = []
                else:
                    temp_map[wiz_tuple[0]] += [wiz_tuple[1]]
        print(temp_map)

    def solve(self, wizards, constraints):
        wizards = sorted(wizards)
        constraints = self.prune_constraints(constraints)
        self.generate_variables(wizards)
        self.generate_transitivity_clauses(wizards)
        self.generate_constraint_clauses(wizards, constraints)
        self.generate_additional_clauses()
        pycosat_result = self.solve_SAT()
        if type(pycosat_result) != list:
            raise Exception(pycosat_result) #e.g. UNSAT
        return self.find_ordering(wizards, pycosat_result)

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