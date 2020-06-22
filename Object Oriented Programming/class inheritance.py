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

    # class method Property
    @classmethod
    # craeting a Function of Type Class Method
    def from_string(cls, emp_string):
        # splitting the fname lname and salary from the String
        fname, lname, salary = emp_string.split("-")
        # returning the Extracted Values
        return cls(fname, lname, salary)

    @staticmethod                                               # Class Static Method
    def is_open(day):                                           # creating a function
        if day == "sunday" or day == "Sunday":                  # checking the Condition
            # returning on the basis of the output
            return False
        else:
            # returning the Alternate output on the basis of if statement
            return True


# creating anathor class
class Programmer(Employee):
    # creating a Constructor of Second Class
    def __init__(self, fname, lname, salary, proglang, exp):
        # calling the Constructor of the Employee Class
        super().__init__(fname, lname, salary)
        # Setting the Value to the Variable
        self.proglang = proglang
        # Setting the Value to the Variable
        self.exp = exp


# creating a Object of Class Programmer and Assigning Values to the object
harry = Programmer("Alex", "Mercer", 44000, "Python", "5 Years")
print(harry.fname, harry.lname,                                 # Printing The Values
      harry.salary, harry.proglang, harry.exp)
