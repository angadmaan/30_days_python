# Write a program to print the following star pattern:

"""
***
** for n = 3
*** 
"""

n = int(input("Enter your number: "))

for i in range(n, 0, -1):
    print("*" * i)
