# creating a Class of name Employee
class Employee:

    # creating a Class Variable
    increament = 1.5

    # Creating a Constructor of the Class Employee
    def __init__(self, fname, lname, salary):
        # setting Values to the variables
        self.fname = fname
        # setting Values to the variables
        self.lname = lname
        # setting Values to the variables
        self.salary = salary

    def increase(self):                                         # Creating a Constructor
        # making a change in the Class variable
        self.salary = int(self.salary * Employee.increament)


# creating Objects of the Class Employee
alex = Employee("Alex", "Mercer", 44000)
harry = Employee("Harry", "Bhai", 44000)
# Increasing the Salary of the Alex Object
alex.increase()
# printing the Salary of the alex Object
print(alex.salaray)
# printing all the Elements of the Alex Object
print(alex.__dict__)
# printing all the Elements of the Employee Class
print(Employee.__dict__)
