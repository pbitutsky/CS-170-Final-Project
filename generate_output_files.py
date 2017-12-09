import Solver
import output_validator
import randomAlt
from os import listdir
from os.path import isfile, join


def generate_output_files(num_wizards):
    for i in range(0, 10):
        infile = 'phase2_inputs/inputs{0}/input{0}_{1}.in'.format(num_wizards, i)
        outfile = 'outputs/output{0}_{1}.out'.format(num_wizards, i)
        try:
            Solver.main(infile, outfile)
            output_validator.main([infile, outfile])
            print("success")
        except:
        	print("error")


def staff_inputs():
    inputs = [60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]
    for input in inputs:
        infile = 'Staff_Inputs/staff_{0}.in'.format(input)
        outfile = 'outputs/staff{0}.out'.format(input)
        try:
            Solver.main(infile, outfile)
            output_validator.main([infile, outfile])
            print(str(input) + "success")
        except:
        	print("error")

# staff_inputs()

def phase3():
    inputs = [f for f in listdir('assigned_input_submissions') if isfile(join('assigned_input_submissions', f))]
    print(len(inputs))
    # for input in inputs:
    #     file_without_extension = input[:-3]
    #     print(file_without_extension)
    #     infile = 'assigned_input_submissions/{0}.in'.format(file_without_extension)
    #     outfile = 'outputs/{0}.out'.format(file_without_extension)
    #     try:
    #         Solver.main(infile, outfile)
    #         output_validator.main([infile, outfile])
    #         print(str(input) + "success")
    #     except:
    #         print("error")



def phase3_problematic():
    problematic = ['submission_4714364_input35', 'submission_4714433_input50', 'submission_4620699_input20', 'submission_4714128_inputs_input20']
    for input in problematic:
        infile = 'assigned_input_submissions/{0}.in'.format(input)
        outfile = 'assigned_input_submissions/{0}.out'.format(input)

        Solver.main(infile, outfile)
        output_validator.main([infile, outfile])
        print(str(input) + "success")

# phase3_problematic()
phase3()