class Employee:
    company = "ITC"
    name = "priyanka"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

'''
class programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is good with {self.language} language")
'''

class programmer(Employee):
    company = "ITC Infotech"
    name = "sandip"
    def showLanguage(self):
        print(f"The name of the employee is {self.name} and he is good with {self.language} language")
a = Employee()        
b = programmer()


print( a.name, a.company)
print( b.name, b.company)

