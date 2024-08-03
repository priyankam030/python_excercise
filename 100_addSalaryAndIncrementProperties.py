'''
Create a class 'Employee' and add the salary and increment it to do
'''
from random import randint


class Employee:
    salary = 1200000
    def salari(self):
        print(f"The salary is: {self.salary}.")

    def increment(self):
        print(f"Increment is: {randint(10, 20)}%")

priya = Employee()

priya.salari()
priya.increment()