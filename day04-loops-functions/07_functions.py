# Functions in python are defined using the def keyword. The function name is followed by parentheses and a colon. The body of the function is indented.

# They are used to group a set of statements together so they can be run more than once. Functions can take parameters and return values.

# In simple language, a peice of logic is given a name and can be reused multiple times in a program.

def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = (a + b) / 2
    print("Average of two numbers is: ", c)

avg()  # Calling the function to execute it [Function call]

print("Thank You!")

avg()

print("Goodbye!")



# Types of functions in python:

# 1. Built-in functions: These are functions that are already defined in Python and can be used directly without any additional code. Examples include print(), len(), type(), etc.
# 2. User-defined functions: These are functions that are defined by the user to perform specific tasks. The avg() function defined above is an example of a user-defined function.


# Function with arguments: 

def goodDay(name, ending):
    print("Have a good day!, " + name)
    print(ending)
    return "Good Bye!" # Return value used to store a value in variable.
goodDay("Angad ", "Thank you!")
goodDay("Rohan ","Thanks!")

a = goodDay("Rahul", "Hola!")
print(a)


# Default arguments: If a function is called without an argument, the default value is used. [Default Parameter Value]

def goodDay(name, ending = "Thank you!"):
    print(f"Have a good day!, {name}")
    print(ending)

goodDay("Angad")
