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


# printing the Vlaues with Diffrent Inputs
print(Employee.is_open("Sunday"))
print(Employee.is_open("sunday"))
print(Employee.is_open("Monday"))
# lovish = Employee.from_string("lovish-jakson-76000")
# print(lovish.fname, lovish.lname, lovish.salary)
