f = open('test.txt') # Open that files and store in variable f then you can perform any action to f

# fr = f.read() # Read the file in this case test.txt

# seek = f.seek(0) # Returns the beginning of the file

# read_line = f.readlines() # Go through every line and return list

# for line in open('test.txt'):
for line in f:
    print(line)

