import pycosat

matrix = [[letter + str(number) for number in range(1, 5)] for letter in ['a', 'b', 'c', 'd']]
for row in matrix:
    print(row)
n = len(matrix)

row_col_to_num = lambda row, col: n*row+col+1
num_to_row_col = lambda num: ((num-1) // n, (num - 1) % n)
lookup = lambda num: matrix[num_to_row_col(num)[0]][num_to_row_col(num)[1]]

#O(n^3)
cnf_input = []
for col in range(0, n):
    for row in range(0, n):
        for row2 in range(row+1, n):
            english = "If "+matrix[row][col]+" then not "+matrix[row2][col]
            cnf = "¬"+matrix[row][col]+" ∨ "+"¬"+matrix[row2][col]
            cnf2 = [-(n*row+col+1), -(n*row2+col+1)]
            cnf_input.append(cnf2)
            print(english, "    ", cnf, "    ", cnf2)

print("\n")
for row in range(0, n):
    for col in range(0, n):
        for col2 in range(col+1, n):
            english = "If "+matrix[row][col]+" then not "+matrix[row][col2]
            cnf = "¬"+matrix[row][col]+" ∨ "+"¬"+matrix[row][col2]
            cnf2 = [-(n*row+col+1), -(n*row+col2+1)]
            cnf_input.append(cnf2)
            print(english, "    ", cnf, "    ", cnf2)

#O(n^2)
for col in range(0, n):
    cnf_input.append([(n*row+col+1) for row in range(0, n)])

for row in range(0, n):
    cnf_input.append([(n * row + col + 1) for col in range(0, n)])

letter_to_col_map = {'a': 1, 'b': 2, 'c':3, 'd':4}
constraints = [['a', 'b', 'c']]
for constraint in constraints:
    # Katya this is where you come in
    pass

tmp_list = [
    ['a1', 'b3', 'c2'],
    ['a1', 'b4', 'c2'],
    ['a1', 'b4', 'c3'],
    ['a2', 'b4', 'c3'],
    ['b1', 'a3', 'c2'],
    ['b1', 'a4', 'c2'],
    ['b1', 'a4', 'c3'],
    ['b2', 'a4', 'c3']
]

# returns a list of cnf clauses
def expand_constraint():
    pass

def find(letter):
    for row in range(0, n):
        for col in range(0, n):
            if matrix[row][col] == letter:
                return (n*row+col+1)
    return -1

for tmp in tmp_list:
    cnf_input.append([-find(tmp[0]), -find(tmp[1]), -find(tmp[2])])

for row in cnf_input:
    print(row)

result = pycosat.solve(cnf_input)
print(result)
print([num_to_row_col(r) for r in result if r > 0])
print([lookup(r) for r in result if r > 0])
