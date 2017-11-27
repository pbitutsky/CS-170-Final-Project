from shutil import copyfile

f = open('assigned_inputs', 'r')
files = str(f.readline()).split(",")
for file in files:
    if file: # I think the empty string or carriage return or something messes it up so this line helps
        src = "all_submissions/" + file
        dst = "assigned_input_submissions/" + file
        copyfile(src, dst)