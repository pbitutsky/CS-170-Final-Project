import traceback
from search import *
from random import *
import string
import random

import sys
if sys.version_info[0] < 3:
    raise "Must be using Python 3"

def read_file_and_search(file_name):
    def test():
        file = open(file_name, "r")
        W = int(file.readline())
        wizards = str(file.readline()).strip().split(" ")
        C = int(file.readline())
        constraints = list()
        for i in range(C):
            wizard1, wizard2, wizard3 = str(file.readline()).strip().split(" ")
            constraints.append([wizard1, wizard2, wizard3])
        return search(constraints, len(wizards))
    return test

def random_test(num_wizards):
    # generate a list of n random names of length 10, and constraints
    lst = [''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) for i in range(num_wizards)]
    # C = random.randint(1, 10)
    C = 500
    constraints = list()
    for i in range(C):
        # generate a random constraint
        wizards_to_constrain = [lst[j] for j in sorted(random.sample(range(0, num_wizards), 3))]
        if random.randint(0, 1):
            if random.randint(0, 1):
                wizard1, wizard2, wizard3 = wizards_to_constrain
            else:
                wizard2, wizard1, wizard3 = wizards_to_constrain
        else:
            if random.randint(0, 1):
                wizard3, wizard2, wizard1 = wizards_to_constrain
            else:
                wizard3, wizard1, wizard2 = wizards_to_constrain
        constraints.append([wizard1, wizard2, wizard3])

    def test():
        return search(constraints, num_wizards)
    return test

tests = {
    # "Input20": read_file_and_search("input20.in"),
    # "Input35": read_file_and_search("input35.in")
     "Random16": random_test(16)
         }

for i in range(17, 25):
    tests["Random"+str(i)] = random_test(i)

counter = 0
passed = 0
for key in tests:
    test = tests[key]
    print("Starting", key)
    test_results = test()
    if test_results:

        print(counter, key + ": ", "Passed!")
        print(test_results)
        passed += 1
    else:
        print(counter, key + ": ", "Failed! ")
        print(test_results)
        sys.exit(0)
    counter += 1

print("")
print(passed, "tests passed.")



