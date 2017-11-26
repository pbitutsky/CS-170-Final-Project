import traceback
from search import *

from Solver import *

s = Solver()
solve = s.solve


def read_file_and_solve(file_name):
    file = open(file_name, "r")
    W = int(file.readline())
    wizards = str(file.readline()).strip().split(" ")
    C = int(file.readline())
    constraints = list()
    for i in range(C):
        wizard1, wizard2, wizard3 = str(file.readline()).strip().split(" ")
        constraints.append([wizard1, wizard2, wizard3])
    print(solve(sorted(wizards), constraints))

def read_file_and_search(file_name):
    file = open(file_name, "r")
    W = int(file.readline())
    wizards = str(file.readline()).strip().split(" ")
    C = int(file.readline())
    constraints = list()
    for i in range(C):
        wizard1, wizard2, wizard3 = str(file.readline()).strip().split(" ")
        constraints.append([wizard1, wizard2, wizard3])
    print(search(constraints, len(wizards)))

def make_test_simple(correct_list, constraints):
    # if type(correct_list) == list:
    #     correct_ordering = lst_to_ordering(correct_list)
    # elif type(correct_list) == dict:
    #     correct_ordering = correct_list
    # else:
    #     raise Exception("You need to pass in either a list or a dict")

    def test_simple():
        try:
            test_result = search(constraints,len(correct_list))
            total_passed = constraint_satisfaction(test_result, constraints)[0]
            if total_passed == len(constraints): #passed all constraints
                return True, ""
            else:
                return False, "Solve returned an ordering that does not satisfy all constraints."
        except Exception as e:
            print(traceback.print_exc())
            return False, "Exception Raised!"

    return test_simple

def make_test_simple_search(correct_list, constraints):
    # if type(correct_list) == list:
    #     correct_ordering = lst_to_ordering(correct_list)
    # elif type(correct_list) == dict:
    #     correct_ordering = correct_list
    # else:
    #     raise Exception("You need to pass in either a list or a dict")

    def test_simple():
        try:
            test_result = search(constraints,len(correct_list))
            # total_passed = constraint_satisfaction(test_result, constraints)[0]
            # if total_passed == len(constraints): #passed all constraints
            if test_result is not None:
                return True, ""
            else:
                # return False, "Solve returned an ordering that does not satisfy all constraints."
                return False, ""
        except Exception as e:
            print(traceback.print_exc())
            return False, "Exception Raised!"

    return test_simple


tests = {

    "Simple 8 letters": make_test_simple_search(['d', 'b', 'g', 'h', 'f', 'e', 'c', 'a'],
                                      [['c', 'b', 'a'], ['e', 'c', 'b'], ['a', 'c', 'h'], ['a', 'e', 'g'],
                                       ['f', 'd', 'e'], ['c', 'f', 'd'], ['g', 'c', 'd'], ['b', 'f', 'd'],
                                       ['b', 'a', 'd'], ['b', 'f', 'c'], ['g', 'e', 'd'], ['a', 'f', 'g'],
                                       ['f', 'b', 'd'], ['e', 'a', 'f'], ['c', 'e', 'b']]),
    "Game of Thrones": make_test_simple_search(["Sansa", "Rickon", "Jon", "Rob", "Bran", "Arya"],
                                        [["Jon", "Sansa", "Rob"], ["Jon", "Arya", "Rob"],
                                         ["Jon", "Bran", "Rob"], ["Sansa", "Rickon", "Jon"],
                                         ["Arya", "Rickon", "Jon"], ["Bran", "Rickon", "Jon"],
                                         ["Arya", "Bran", "Jon"], ["Sansa", "Rob", "Rickon"],
                                         ["Arya", "Rob", "Bran"], ["Sansa", "Rickon", "Rob"]])
}

counter = 0
passed = 0
for key in tests:
    test = tests[key]
    did_pass_test, message = test()
    if did_pass_test:
        print(counter, key + ": ", "Passed!")
        passed += 1
    else:
        print(counter, key + ": ", "Failed! " + message)
    counter += 1

print("")
print(passed, "tests passed.")

read_file_and_search("input20.in")
read_file_and_search("input35.in")

