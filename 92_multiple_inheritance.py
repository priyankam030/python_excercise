'''
          parent1   +   parent2   =   child

'''
class Employee:
    company = "ITC"
    name = "Priyanka"
    def show(self):
        print(f"The name of the employee is {self.name} and The company name  is {self.company}")

class coder:
    language = 'python'
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")


class programmer(Employee, coder):
    company = "ITC Tnfotech"
    def showLanguage(self):
        print(f"The company name  is {self.company} and he is good with {self.language} language")
a = Employee()        
b = programmer()

b.show()
b.printLanguage()
b.showLanguage()
