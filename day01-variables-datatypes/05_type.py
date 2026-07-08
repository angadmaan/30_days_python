# Type functions in Python

x = 10
y = "Hello"
z = 3.14

print("Types of variables:")

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

a = "25"
print(type(a))  # <class 'str'>

print("Converting data types:")
b = int(a)  # Convert string to integer
c = float(a)  # Convert string to float
d = str(10)  # Convert integer to string

print(type(b))  # <class 'int'>
print(type(c))  # <class 'float'>
print(type(d))  # <class 'str'>