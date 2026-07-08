# Check the type of variable assigned using input() function and print the result.

num = (input("Enter a number: "))
print("The type of the variable is:", type(num)) # Always returns <class 'str'> because input() function always returns a string.


num1 = int(input("Enter a number: "))
print("The type of the variable is:", type(num1))
