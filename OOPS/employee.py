class Employee:
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +last + '@gmail.com'
    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    
emp_1 = Employee("anisha", "nayaju", 100000)
emp_2 = Employee("arica", "shrestha", 70000)

# print(emp_1.fullname())
# print(emp_2.fullname())
print(Employee.fullname(emp_1))
