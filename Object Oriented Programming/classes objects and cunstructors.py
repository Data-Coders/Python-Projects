# creating a Class of name Employee
class Employee:

    # Creating a Constructor of the Class Employee
    def __init__(self, fname, lname, salary):
        # setting Values to the variables
        self.fname = fname
        # setting Values to the variables
        self.lname = lname
        # setting Values to the variables
        self.salary = salary


# creating a Object using a String
alex = Employee("Alex", "Mercer", 4400)
harry = Employee("Harry", "Bhai", 4400)

# printing the Values
print(alex.fname, alex.lname, alex.salaray)
print(harry.fname, harry.lname, harry.salaray)
