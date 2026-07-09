# Write a program to sum a list of 4 numbers entered by the user.

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

num3 = int(input("Enter the third number: "))

num4 = int(input("Enter the fourth number: "))  

numbers = [num1, num2, num3, num4]

total_sum = sum(numbers)

print("The sum of the numbers is:", total_sum)