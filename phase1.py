import random
import string

def generate_random_constrains():
    for n in [20, 35, 50]:
        #generate a list of n random names of length 10, and constraints
        lst = [''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) for i in range(n)]
        # C = random.randint(1, 10)
        C = 500
        constraints = list()
        for i in range(C):
            #generate a random constraint
            wizards_to_constrain = [lst[j] for j in sorted(random.sample(range(0, n), 3))]
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

        print("Correct Order: ", lst)
        print("Constraints: ", constraints)
        ordering = {lst[i]: i+1 for i in range(len(lst))}

        f = open('input' + str(n) + '.in', 'w')
        f.write(str(len(lst)) + '\n')
        f.write(' '.join(lst) + '\n')
        f.write(str(len(constraints)) + '\n')
        for constraint in constraints:
            f.write(' '.join(constraint) + "\n")