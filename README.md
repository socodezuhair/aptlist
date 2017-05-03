# Apartment List Exercise
README file for the Aparment List coding exercise

## Approach:
Based on the requirements, I first tried to figure out how to shuffle the list and how to break it up
appropriately.  The requirements were random groups and groups should be no smaller than three and no bigger than five.

While perhaps not ideal, I decided to make the default group size equal to 3.  So, the idea is to find as many groups of three people as I can find and then fit the rest into a group of 4 or 5 people.  My approach was to find the count of total employees, mod by 3 and then use the remainder for the last group.

I started off by just creating a simple list from the alphabet to put the basic code in place.  The letters of the alphabet can later be replaced by employee names.  I shuffle the list and then break it up into appropriate groups, having print statements along the way to debug the code.  This approach generally works and we don't get a group bigger than five.

Since the general approach worked, I productionalized the code to include the other features such as adding an employee.

This included creating a text file with the names of the employees.  The program will read the file to get a list of all the employees.  The add and remove functionality updates the file accordingly, using the name of the employee entered by the user.

I also optimized the code a little bit.

## Documentation
The program is simple enough and will prompt the user for what to do.

### Requirements
Python 2 is installed

### To execute:
- clone repo
- run the command: python aptlist.py
