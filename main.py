#Class, object, constructor

class Employee:
    def __init__(self, fname, lname, salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary

    pass 

vivek = Employee('vivek', 'vyas', '25000')
dhruv = Employee('dhruv', 'das', '25000')

print(vivek.lname, dhruv.fname)

# class(blueprint/template) -> Employee
# object -> vivek, dhruv
# That object holds the data (attributes) fname, lname, and salary