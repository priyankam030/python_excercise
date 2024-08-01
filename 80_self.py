class Employee:
    language = "py" # This is a class attribute
    salary = 1300000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
 

harry = Employee()    # Here harry is an object
harry.language = "javaScript" # This is an instance attribute
harry.getInfo()

# Employee.getInfo(harry)

