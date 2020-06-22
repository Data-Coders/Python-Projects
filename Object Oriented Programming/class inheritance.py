class Employee:

    increament = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increament)

    @classmethod
    def change_increament(cls, amount):
        cls.increament = amount

    @classmethod
    def from_string(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def is_open(day):
        if day == "sunday" or day == "Sunday":
            return False
        else:
            return True


class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp


harry = Programmer("Alex", "Mercer", 44000, "Python", "5 Years")
print(harry.fname, harry.lname, harry.salary, harry.proglang, harry.exp)
