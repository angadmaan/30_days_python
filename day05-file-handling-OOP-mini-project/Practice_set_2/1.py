# Create a class Programmer for storing information of few programmers who work at Microsoft.

class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

angad = programmer("Angad", 1300000, 1432234)
print(angad.name, angad.salary, angad.pincode, angad.company)

raj = programmer("Rajkumar", 500000, 1532234)
print(raj.name, raj.salary, raj.pincode, raj.company)

