# Write a program to detect double space in a string and replace it with single space.

name = input("Enter a string: ")
double_space_detected = name.find("  ")

print(name.replace("  ", " ")) 

if double_space_detected != -1:
    print("Double space detected and replaced.") # Strings are immutable, so we need to assign the replaced string to a new variable or print it directly.
else:
    print("No double space detected.")