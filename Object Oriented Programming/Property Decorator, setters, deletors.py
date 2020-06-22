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

    # creating a Function to Override the Default Function in the Python Compiler
    def __repr__(self):
        # setting the value according to the Need
        return f"The Name of this Employee is : {self.fname} {self.lname}\nThe Salary of this Employee is : {self.salary} "

    # creating a Function to Override the Default Function in the Python Compiler
    def __str__(self):
        # setting the value according to the Need
        return f"{self.fname} is a Employee of Abstergo Insdustries Ltd."

    # class property of the Class
    @property
    # creating a Funtion to set the email of the Employee
    def email(self):
        # returning the Employees Email adress according to its name and Last name
        return self.fname.lower() + "." + self.lname.lower() + "@email.com"

    # setter property of Class
    @email.setter
    # creating a function to make the need changed
    def email(self, given_email):
        # splitting the email provided by the User
        name_list = given_email.split('@')[0].split('.')
        # assigning the Value
        self.fname = name_list[0]
        self.lname = name_list[1]


# creating a object of Employee Class
harry = Employee("Harry", "Bhai", 44000)
# printing its Default email adress
print(harry.email)
# changing its Title to some other last name
harry.lname = "Khanna"
# now printingto see if the Change has been made
print(harry.email)
# giving the email we want to keep as default
harry.email = "khanna.harry@email.com"
# now finalising the Email if Everything gone Correct
print(harry.email)
