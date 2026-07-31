# Write a program to print multiplication table of a given number using for loop and while loop.


n = int(input("Enter Your Number: "))

print("With for loop")

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")

print("\nWith while loop")

i = 1

while(i<11):
    print(f"{n} X {i} ={n*i}")

    i += 1 # i = i+1

