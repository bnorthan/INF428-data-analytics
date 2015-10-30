# Author Tiago Ferreira, Brian Northan
# Python01.py
# IJ BAR: https://github.com/tferr/Scripts#scripts

####################################################
# 1. Basics
####################################################

# This is a comment (typically single line)
"""
Triple quotes are used for large multi-line comments, and
typically to document functions and modules (Docstrings)
"""

# Python features a built-in print statement that outputs
# to the Script Editor's console ("Show Output" button). It
# accepts one or more arguments (a string, number, object,
# ...), separated by commas
# NB: In Python 3, the print statement became a function,
# and needs to be flanked by brackets. For details, see
# https://docs.python.org/3.0/whatsnew/3.0.html#print-is-a-function
print "Hello!"
print

# Math works as expected:
a = 1+1		# Sum
b = 2*4		# Multiplication
c = 2**4	# Exponentiation (2^14 = 16)
print "Print variables a, b, c", a, b, c
print

# Division is slightly special:
print "Integer division: 3/4=", 3/4
print "Float division: 3/4=", 3.0/4.0
print

# BTW, you cal also multiply strings. Try this:
print "Multiply hello by 3: ", 3*"Hello!"
print

# Operators:
print "(a is b):", (a is b)
print "a==2:", a==2
print "a is not b and b!=2:", a is not b and b!=2
print

# Working with lists: Lists are indexed sequences of items. The
# 1st index (item position) is zero, the 2nd index is one, etc.
my_list =[]				# An empty list
my_list = [1,2,3,4,5,6]	# A prefilled list
my_list[0] = "string"	# Assign new value to an initialized index
my_list.append(7)		# Append new item to list
print "Here is the list:", my_list
my_list.pop()			# Remove last element from list
print "And here it is after calling list.pop():", my_list
print

# Working with dictionaries: Dictionaries store mappings between
# <keys> and <values>. Keys can be unique strings or numbers (or
# any immutable type). Values can be anything: a string, a number,
# an expression, or any other object.
my_dict = {}								# An empty dictionary
my_dict = {"John":1234, "my_list":my_list}	# A prefilled dictionary
my_dict['Best Team']="Blue Jays"		# Add a key:value pair

# Create a list from a generator expression (the <value>) and
# associate it to a variable (the <key>)
a = "Bit-depths"
my_dict[a] = [2**x for x in (1, 8, 16, 32)]

# Looking up values:
print "my_dict[\"Best Team\"]", my_dict["Best Team"]
print "my_dict[\"my_list\"]", my_dict["my_list"]
print "my_dict[a]", my_dict[a]
try:
    my_var = my_dict["Mojito"]
except KeyError:
    print "Bummer: Mojito is not in the dictionary"
print

## To address later on: Tuples and Sets. See documentation at
## https://docs.python.org/2.7/tutorial/datastructures.html
