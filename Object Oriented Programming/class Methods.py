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

    # class method Property
    @classmethod
    # craeting a Function of Type Class Method
    def change_increament(cls, amount):
        # making change in Class Variable
        cls.increament = amount


# creating Objects of the Class Employee
alex = Employee("Alex", "Mercer", 44000)
harry = Employee("Harry", "Bhai", 44000)
# printing the Salary of the Employee using class
print(alex.salaray)
# Increament of Change in Salary
Employee.change_increament(2)
# changing both the employees Salary
alex.increase()
harry.increase()
# printing Employee 1 Salary
print(alex.salaray)
