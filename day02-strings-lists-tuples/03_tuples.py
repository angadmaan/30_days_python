# Tuples in python are immutable sequences, meaning that once a tuple is created, its elements cannot be changed, added, or removed. Tuples are defined by enclosing elements in parentheses `()` and separating them with commas.

a = (1, 2, 3, 4, 5, False, "Hello", "Joe")  # A tuple of mixed data types.

print(type(a))  # Output: <class 'tuple'>

# Accessing tuple elements

print(a[0])  # Output: 1

print(a[1])  # Output: 2

print(a[2])  # Output: 3

print(a[3])  # Output: 4

print(a[4])  # Output: 5

print(a[5])  # Output: False

print(a[6])  # Output: Hello

print(a[7])  # Output: Joe

# Tuples are immutable, meaning that their elements cannot be changed after they are created. However, you can create a new tuple by concatenating existing tuples or by using slicing.

# Empty tuple
empty_tuple = ()  # An empty tuple.

# Tuple with one element
single_element_tuple = (42,)  # A tuple with a single element. Note the comma after the element, which is necessary to distinguish it from a regular parenthesis otherwise it would be considered an integer.

# Example

single_element_tuple_example = (42)  # This is not a tuple, it's an integer.

print(type(empty_tuple))  # Output: <class 'tuple'>

print(type(single_element_tuple))  # Output: <class 'tuple'>

print(type(single_element_tuple_example))  # Output: <class 'int'>

# Tuple methods

t = (1, 2, 3, 2, 4, 2)  # A tuple of integers.

print(t.count(2))  # count(): This method returns the number of occurrences of a specified element in the tuple.

print(t.index(3))  # index(): This method returns the index of the first occurrence of a specified element in the tuple. If the element is not found, it raises a ValueError.

