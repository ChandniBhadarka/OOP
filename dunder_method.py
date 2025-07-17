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
        
    #1st method
    def __add__(self, other):
        return self.salary + other.salary
    
    #2nd method
    def __repr__(self):
        return 'Employee ({}, {}, {})'.format(self.fname, self.lname, self.salary)
    

vivek = Employee('vivek', 'vyas', 25000)
dhruv = Employee('dhruv', 'das', 25000)

print(vivek+dhruv)


#2nd method
print(repr(vivek))