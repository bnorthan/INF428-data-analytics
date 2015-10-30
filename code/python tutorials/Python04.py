# Author Tiago Ferreira, Brian Northan
# Python04.py
# IJ BAR: https://github.com/tferr/Scripts#scripts
####################################################
# 4. Functions and modules
####################################################

# Functions are defined with <def>. Return values are
# specified by a <return> statement. Here is a function
# without arguments:
def today():
    """This function returns a string of today's date"""
    import datetime		# https://docs.python.org/2/library/datetime.html
    td = datetime.date.today()
    return td

print "today() returned", today()
print  "str(today()) returned", str(today())	# https://docs.python.org/2/library/functions.html?highlight=str()


# A Function with arguments:
def minFunction(a, b):
    """This function returns the smallest of two arguments"""
    if a < b:
        return a
    else:
        return b

print minFunction(10,20), "is smaller"


# NB: Python already features a built-in function that returns the
# smallest of two or more arguments. Try this:
print "The smallest of all is", min(10,20,-10,"-20")	# https://docs.python.org/2/library/functions.html?highlight=min()


# A practical scenario: Try to import something that may not be present.
# If we cannot find it, we try to define it in some other way so that the
# script can progress. In this example, we are trying to use the function
# <theBestDrinkEver> from the (rather fictitious) module <cocktail>
def myFakeFunction(a, b):
    """This function mixes a and b in the right amount
       if the fictitious cocktail module is installed """
try:
    from teams import theBestTeamEver
    print "theBestTeamEver was imported"
except ImportError:
    print "Please install the team package!"
    def theBestTeamEver():
        return "Blue Jays!"

print "The best team ever is " + theBestTeamEver()


# Modifying global variables from within functions: Python wants you to
# confirm that the function is really expected to modify a global variable
# declared outside its scope, by explicitly using the <global> keyword:
best_team = "Yankees"

def set_best_team_to_blue_jays():
    global best_team
    best_team = "Blue Jays"

def set_best_team_to_red_sox():
    best_team = "Red Sox"

print "Best team: " + best_team
set_best_team_to_red_sox() # This will have no effect

print "Best team should still be Yankees: " + best_team
set_best_team_to_blue_jays() 
print "Best team should now be Blue Jays: " + best_team

## To know more:
# http://www.jython.org/jythonbook/en/1.0/DefiningFunctionsandUsingBuilt-Ins.html
