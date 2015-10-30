# Author Tiago Ferreira, Brian Northan
# Python02.py
# IJ BAR: https://github.com/tferr/Scripts#scripts
####################################################
# 2. If statements and for loops
####################################################

a,b = 10,20
my_list = [1, 2, 3, 4]

# An if statement: Indentation is critical in python!
if a in my_list:
	print a, "is in the list"
elif b in my_list:
	print b, "is in the list"
else:
    print "Neither", a, "or", b, "are in in the list"

# the range function simply returns a list of numbers in the specified range
range_list=range(354,363)

print
print "the range_list is: ", range_list
print

# the range function is useful for creating for loops
print "Line 19:", "Integers between 5 and 10:"
for i in range(5, 10):
    print "i is: ", i

# Looping through lists:
# NB: For Python's buil-in functions (such as <str()> see
# https://docs.python.org/2/library/functions.html

print
print "Loop through a list"
for team in ["Blue Jays", "Yankees", "Red Sox", "Rays", "Orioles"]:
    print "The team is: ", team

## To address later on: enumerate(). See documentation at
## https://docs.python.org/2/library/functions.html#enumerate
