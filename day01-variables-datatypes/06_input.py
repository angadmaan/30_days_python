# Input function in Python allows the user to take input from the console. The input is always taken as a string, so if you want to take numerical input, you need to convert it to the appropriate data type.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name)
print("You are", name, "and you are", age, "years old.")