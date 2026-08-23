# The with statement automatically handles closing the file after its suite finishes, even if an exception is raised. This makes it a preferred way to work with files in Python.

with open("file.txt") as f:
    print(f.read())

# You don't have to explicitly call f.close() when using the with statement, as it takes care of that for you.

