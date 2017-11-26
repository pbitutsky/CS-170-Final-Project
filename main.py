# import random
# import string
#
# # file = open("test2.in", "r")
# # W = int(file.readline())
# # wizards = str(file.readline()).strip().split(" ")
# # C = int(file.readline())
# # constraints = list()
# # for i in range(C):
# #     wizard1, wizard2, wizard3 = str(file.readline()).strip().split(" ")
# #     constraints.append([wizard1, wizard2, wizard3])
# # ordering = {"Albus": 1, "Severus": 2, "Hermione": 3, "Harry": 4}
# # ordering = {"Hermione": 1, "Harry": 2, "Severus": 3, "Albus": 4}
#
#
# # ordering = {"Albus": 1, "Hermione": 2, "Severus": 3, "Harry": 4}
# # opp_order = {ordering[key]: key for key in ordering}
# # lst = ["Rob", "Jon", "Sansa", "Arya", "Bran", "Rickon"]
# # lst = ["a", "b", "c", "d", "e", "f", "g", "h"]
# n = 16
# lst = [''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) for i in range(n)]
# random.shuffle(lst)
# # lst = ['Rob', 'Jon', 'Rickon', 'Bran', 'Arya', 'Sansa']
# # ordering = {lst[i]: i+1 for i in range(len(lst))}
# # print(lst)
# C = 500
#
# constraints = list()
# for i in range(C):
#     #generate a random constraint
#     wizards_to_constrain = [lst[j] for j in sorted(random.sample(range(0, n), 3))]
#     if random.randint(0, 1):
#         if random.randint(0, 1):
#             wizard1, wizard2, wizard3 = wizards_to_constrain
#         else:
#             wizard2, wizard1, wizard3 = wizards_to_constrain
#     else:
#         if random.randint(0, 1):
#             wizard3, wizard2, wizard1 = wizards_to_constrain
#         else:
#             wizard3, wizard1, wizard2 = wizards_to_constrain
#     constraints.append([wizard1, wizard2, wizard3])
#
#
# print("Correct Order: ", lst)
# print("Constraints: ", constraints)
#
#
#
#
#
#
#
#
#
#
#
# # correct_lst = ['d', 'b', 'g', 'h', 'f', 'e', 'c', 'a']
# # constraints = [['c', 'b', 'a'], ['e', 'c', 'b'], ['a', 'c', 'h'], ['a', 'e', 'g'], ['f', 'd', 'e'], ['c', 'f', 'd'], ['g', 'c', 'd'], ['b', 'f', 'd'], ['b', 'a', 'd'], ['b', 'f', 'c'], ['g', 'e', 'd'], ['a', 'f', 'g'], ['f', 'b', 'd'], ['e', 'a', 'f'], ['c', 'e', 'b']]
#
# # constraints = [["Jon", "Sansa", "Rob"], ["Jon", "Arya", "Rob"], ["Jon", "Bran", "Rob"], ["Sansa", "Rickon", "Jon"], ["Arya", "Rickon", "Jon"], ["Bran", "Rickon", "Jon"], ["Arya", "Bran", "Jon"], ["Sansa", "Rob", "Rickon"], ["Arya", "Rob", "Bran"], ["Sansa", "Rickon", "Rob"]]
# # print(solve(["Sansa", "Rickon", "Jon", "Rob", "Bran", "Arya"], constraints))
#
# print(solve(sorted(lst), constraints))