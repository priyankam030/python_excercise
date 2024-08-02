class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

'''
class programmer:
    company = "ITC Tnfotech"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is good with {self.language} language")
'''

class programmer(Employee):
    company = "ITC Tnfotech"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is good with {self.language} language")
a = Employee()        
b = programmer()

print(a.company, b.company)
