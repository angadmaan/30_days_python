# Operators in Python

# Arithmetic Operators
# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# // (Floor Division)
# % (Modulus)
# ** (Exponentiation)

# Comparison Operators
# == (Equal)
# != (Not Equal)
# < (Less Than)
# > (Greater Than)
# <= (Less Than or Equal To)
# >= (Greater Than or Equal To)

# Logical Operators
# and (Logical AND)
# or (Logical OR)
# not (Logical NOT)

# Assignment Operators
# = (Assignment)
# += (Add and Assign)
# -= (Subtract and Assign)
# *= (Multiply and Assign)
# /= (Divide and Assign)
# //= (Floor Divide and Assign)
# %= (Modulus and Assign)
# **= (Exponentiate and Assign)

# Arithmetic Operators

a = 10
b = 5
c = a + b  # Addition
d = a - b  # Subtraction
e = a * b  # Multiplication
f = a / b  # Division   

print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)


# Assignment Operators
a = 10
a += 5  # Add and Assign (a = a + 5)
a -= 3  # Subtract and Assign (a = a - 3)
a *= 2  # Multiply and Assign (a = a * 2)
a /= 4  # Divide and Assign (a = a / 4)

print("Final value of a:", a)

# Comparison Operators
x = 10
y = 5
is_equal = x == y  # Equal
is_not_equal = x != y  # Not Equal
is_less_than = x < y  # Less Than
is_greater_than = x > y  # Greater Than
is_less_than_or_equal = x <= y  # Less Than or Equal To
is_greater_than_or_equal = x >= y  # Greater Than or Equal To

print("Is Equal:", is_equal)
print("Is Not Equal:", is_not_equal)
print("Is Less Than:", is_less_than)
print("Is Greater Than:", is_greater_than)
print("Is Less Than or Equal To:", is_less_than_or_equal)
print("Is Greater Than or Equal To:", is_greater_than_or_equal)

# Logical Operators
p = True
q = False   

p and q  # Logical AND
p or q  # Logical OR
not p  # Logical NOT

print("Logical AND:", p and q)
print("Logical OR:", p or q)
print("Logical NOT:", not p)

print("Truth Table for Logical Operators:")

print("Truth table for 'OR' operator:")

print("true or true =", True or True)
print("true or false =", True or False)
print("false or true =", False or True)
print("false or false =", False or False)

print("Truth table for 'AND' operator:")

print("true and true =", True and True)
print("true and false =", True and False)
print("false and true =", False and True)
print("false and false =", False and False)

print("Truth table for 'NOT' operator:")

print("not true =", not True)
print("not false =", not False)

