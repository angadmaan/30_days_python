# Write a program to find whether a given number is prime or not.

n = int(input("Enter your number: "))

for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number")

    break