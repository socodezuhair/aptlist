import random
import string

# Generate employee list by reading from a file
empList = open('employees.txt').read().splitlines()
print("%d total employees" % len(empList))

# Get the mod and div, to be used to create the groups later
divMod = divmod(len(empList), 3)
div = divMod[0]-1
mod = divMod[1]

# Shuffle the list to generate random groups
# This is where the magic happens
random.shuffle(empList,random.random)

print("Shuffled list: %s" % empList)

#Generate groups based on the numbers above.
for x in range(div):
	print("Group #%d: %s" % (x, empList[0:3] ))
	del empList[0:3]

# Print the final group
print("Group #%d: %s" % (x+1, empList[0:mod+3]))
del empList[0:mod+3]

# Check the number of employees without a table
# This can just be the length of our list of employees.  If len(list) == 0, all employees have a seat
print("\nNumber of employees without a table: %d\n" % len(empList))