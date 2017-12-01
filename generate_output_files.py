import Solver
import output_validator
import randomAlt


def generate_output_files(num_wizards):
    for i in range(5, 10):
        infile = 'phase2_inputs/inputs{0}/input{0}_{1}.in'.format(num_wizards, i)
        outfile = 'outputs/output{0}_{1}.out'.format(num_wizards, i)
        # try:
        Solver.main(infile, outfile)
        output_validator.main([infile, outfile])
        # except:
        # 	print("error")


generate_output_files(50)



def random_solve(num_wizards, i):
    infile = 'phase2_inputs/inputs{0}/input{0}_{1}.in'.format(num_wizards, i)
    outfile = 'outputs/output{0}_{1}.out'.format(num_wizards, i)
    # try:
    num_wizards, num_constraints, wizards, constraints = Solver.read_input(infile)
    randomAlt.random_check(constraints, wizards)
    output_validator.main([infile, outfile])

    for i in range(10):
        infile = 'phase2_inputs/inputs{0}/input{0}_{1}.in'.format(num_wizards, i)
        outfile = 'outputs/output{0}_{1}.out'.format(num_wizards, i)
        # try:
        Solver.main(infile, outfile)
        output_validator.main([infile, outfile])
        # except:
        # 	print("error")


# generate_output_files(50)

# random_solve(50, 9)
