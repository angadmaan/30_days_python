# OOPs in Python

# Object oriented programming is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main aim of OOPs is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

# Class: A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

# Object: An object is an instance of a class. It is a self-contained entity that consists of both data and procedures to manipulate the data.

class employee:
    age = "20"              # Class attribute
    language = "Python"
    salary = 1200000


angad = employee()
angad.name = "Angad"
print(angad.name, angad.age, angad.language, angad.salary)

raj = employee()
raj.name = "Rajkumar" # Instance(object) attribute
raj.age = 31
print(raj.name, raj.age, raj.language, raj.salary)

# Here "name" is instance attribute and "age", "language" and "salary" are class attribute as they directly belong to the class. 

# Self parameter: self refers to the current object of a class. It is automatically passed with a function call from an object

class Employee:
    def introduce(self):
        print("Hello, my name is", self.name)

angad = Employee()
angad.name = "Angad"

angad.introduce()

# Static Method: A static method is a method inside a class that does not use self or access the object's data. (Decorator)

class employee:
    @staticmethod
    def greet():
        print("Good Morining!")

angad = employee()
angad.greet()

# Constructor: A constructor is a special method that automatically runs when an object is created. It is used to initialize the object's attributes. 

# Example:  __init__ is a special method that automatically runs when an object is created. It is commonly used to initialize the object's data.

# This runs automatically 

class Employee:
    def __init__(self, name, salary, language): # Except self can take more arguments
        self.name = name
        self.salary = salary
        self.language = language
        print("I am Dunder method!!") # Double Underscore method

angad = Employee("Angad", 1300000, "Python")
print(angad.name, angad.salary, angad.language)

