'''
Create a class 'Employee' and add the salary and increment properties to
it.

Write a method 'salaryAfterIncrement' method with a @property decorator 
with a setter which change the value of increment based on the salary.
'''

class Employee:
    salary = 1200
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return(self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100

priya = Employee()
print(priya.salaryAfterIncrement)
priya.salaryIncrement = 1440

print(priya.increment)