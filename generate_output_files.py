import solver
import output_validator

def generate_output_files(num_wizards):
	for i in range(10):
		infile = 'phase2_inputs/inputs{0}/input{0}_{1}.in'.format(num_wizards, i)
		outfile = 'outputs/output{0}_{1}.out'.format(num_wizards, i)
		# try:
		solver.main(infile, outfile)
		output_validator.main([infile, outfile])
		# except:
		# 	print("error")
		
generate_output_files(50)