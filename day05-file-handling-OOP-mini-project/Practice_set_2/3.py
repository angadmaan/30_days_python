# Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = 0. Does this change the class attribute?

class demo:
    a = 4

o = demo()

print(o.a) # Prints class attribute because instance attribute is not set

o.a = 1 # Instance attribute set!!

print(o.a) # Prints instance attribute because now instance attribute is set

# Hence, no the class attribute doesn't change as if now also print the class attribute it will stay the same.

print(demo.a) # Prints the class attribute

