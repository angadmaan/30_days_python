# Lists in python are used to store multiple items in a single variable. Lists are one of the most versatile data structures in Python and can hold items of different data types, including integers, strings, and even other lists.

name = ["Alice", "24", "Bob", "25", "Charlie", "21", "David", "23"]  # A list of names and their corresponding ages.

# Accessing list elements
print(name[0])  # Output: Alice

print(name[1])  # Output: 24

print(name[2])  # Output: Bob

print(name[3])  # Output: 25    

print(name[4])  # Output: Charlie

print(name[5])  # Output: 21

print(name[6])  # Output: David

print(name[7])  # Output: 23

# Modifying list elements
name[1] = "26"  # Changing Alice's age from 24 to 26

print(name)  # Output: ['Alice', '26', 'Bob', '25', 'Charlie', '21', 'David', '23']

# Elements of list are mutable, meaning they can be changed after the list has been created. You can modify an element by accessing it using its index and assigning a new value to it and these changes will be reflected in the original list no new list is created.

# List methods

l1 = [17, 23, 31, 12, 53]  # A list of integers.

l1.sort()  # Sorts the list in ascending order.

print(l1)  # Output: [12, 17, 23, 31, 53]

l1.reverse()  # Reverses the order of the list.

print(l1)  # Output: [53, 31, 23, 17, 12]

l1.append(45)  # Adds the element 45 to the end of the list.

print(l1)  # Output: [53, 31, 23, 17, 12, 45]

l1.insert(2, 99)  # Inserts the element 99 at index 2.

print(l1)  # Output: [53, 31, 99, 23, 17, 12, 45]

l1.remove(17)  # Removes the first occurrence of the element 17 from the list.

print(l1)  # Output: [53, 31, 99, 23, 12, 45]

l1.pop(2)  # Removes element from an index and returns it.

print(l1)  # Output: [53, 31, 23, 12, 45]


