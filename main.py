class Employee:

    increament = 1.5
    def __init__(self, fname, lname, salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        #self.increament = 1.4

    def increase(self):
        self.salary = self.salary * self.increament
        #self.salary = self.salary * Employee.increament

    @classmethod
    def change_increament(cls, amount):
        cls.increament = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.slipt("-")
        return cls(fname, lname, salary)
    
    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else:
            return True

     
class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp




vivek = Programmer('vivek', 'das', 45000, 'C++', '10 yrs')
print(vivek.exp)


# print(Employee.isopen('sunday'))

# vivek = Employee('vivek', 'vyas', '25000')
# sanya = Employee.from_str("sanya-das-45000")
# dhruv = Employee('dhruv', 'das', '25000')

#class method
# print(vivek.salary)
# Employee.change_increament(3)
# vivek.increase()
# print(vivek.salary)

# print(sanya.salary)


# vivek.increase() # 0 agruement but self is defualt so 1 arguement 
#koi object me function ko call krege toh "self" automatically pass ho jaega

#print(vivek.lname, dhruv.fname)
# print(Employee.__dict__)

# class(blueprint/template) -> Employee
# object -> vivek, dhruv
# That object holds the data (attributes) fname, lname, and salary
