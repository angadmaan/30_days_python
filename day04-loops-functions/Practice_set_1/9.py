# Write a program to print the multiplication table of a number using for loops in reversed order.

n = int(input("Enter the number for which you want the multiplication table: "))

for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")