import random
import string

# Define filename to store list of employees
EMPFILE = 'employees.txt'

# Function to add employee to list
def addEmployee():
	# Prompt to get employee name
	response = raw_input("Please enter employee name (to add): ")
	# Open file and save new employee's name to list
	with open(EMPFILE, "a") as myfile:
		myfile.write("%s\n" % response)

# Function to remove employee from list
def delEmployee():
	# Prompt to get employee name
	response = raw_input("Please enter employee name (to remove): ")
	# Open file and read employees to a list (not efficient if list is very long, but works for us now)
	empList = open(EMPFILE).read().splitlines()
	# Remove employee from list
	empList.remove(response)
	# Write list back to file.  First open file, then write employee list to file
	f = open(EMPFILE, 'w')
	for emp in empList:
		f.write("%s\n" % emp)


# Function to print the list of groups
def printGroupList():
	# Generate employee list by reading from a file
	empList = open(EMPFILE).read().splitlines()
	print("%d total employees" % len(empList))

	# Get the mod and div, to be used to create the groups later
	divMod = divmod(len(empList), 3)
	div = divMod[0]-1
	mod = divMod[1]

	# Shuffle the list to generate random groups
	# This is where the magic happens
	random.shuffle(empList,random.random)

	#print("Shuffled list: %s" % empList)

	#Generate groups based on the numbers above.
	for x in range(div):
		print("Group #%d: %s" % (x, empList[0:3] ))
		del empList[0:3]

	# Print the final group
	print("Group #%d: %s" % (x+1, empList[0:mod+3]))
	del empList[0:mod+3]

	# Check the number of employees without a table
	# This can just be the length of our list of employees.  If len(list) == 0, all employees have a seat
	if (len(empList) == 0):
		print("\nAll employees have a seat\n")
	else:
		print("\nThe following employees were not seated: %s\n" % empList)

# Prompt user for what to do.
print("Welcome to the Apartment List lunch table group generator!\n")
print("Please choose from the following options:\n1.) Get seating chart\n2.) Add employee\n3.) Remove employee\n\n")
response = raw_input("What would you like to do: ")

if (response == '1'):
	printGroupList()
elif (response == '2'):
	addEmployee()
elif (response == '3'):
	delEmployee()
else:
	print("Error:  Input not recognized\n")
