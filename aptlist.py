import random
import string

# Generate list
# Later on, this can be reading from a file/DB
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
	# We need to do this because of the way lists are sliced (zero index versus 1)
	# There could be a more elegant way to do it, just keeping it simple in the
	# interest of time.
	if x > 0:
		start = x*3
	else:
		start = 0
	print("Group #%d: %s" % (x,empList[start:start+3] ))

# Print the final group
print("Group #%d: %s" % (x+1, empList[div*3:(div*3) + 3+mod]))

