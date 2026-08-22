# Recursion in Python: It is a fuction that calls itself. It is used to solve problems that can be broken down into smaller sub-problems of the same type. Recursion is a powerful tool in programming, but it can also lead to infinite loops if not implemented correctly.

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")

# Factorial 5 = 5 X Factorial 4
# Factorial 4 = 4 X Factorial 3
# Factorial 3 = 3 X Factorial 2
# Factorial 2 = 2 X Factorial 1 

# Factorial 1 = 1 
# Factorial 0 = 1

