# Conditional Expressions in python


a = int(input("Enter your age: "))

if (a>=18):
    print("\nYou are eligible for driving license")
elif(a<=0):
    print("\nEnter valid age")
else:
    print("\nYou are not eligible for driving license")


print("Thank you for using the driving license eligibility checker") # This print is out of if-else ladder

# Relational Operators in python 

# Relational operators are used to compare two values.
# They return True if the comparison is true, and False if the comparison is false.

# ==  Equal to
# !=  Not equal to
# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to


# Logical Operators in python

# Logical operators are used to combine two or more conditions.

# and : Returns True if both conditions are true.
# or  : Returns True if at least one condition is true.
# not : Returns the opposite of the condition.


# elif Clause

# if (condition1):

# elif (condition2):

# elif(condition3):

# else:

# this ladder will stop once a condition in an if or elif is met.


# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.

