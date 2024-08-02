class Employee:
    language = "python" # This is a class attribute
    salary = 1300000

harry = Employee()    # Here harry is an object
harry.language = "javaScript" # This is an instance attribute
print(harry.language, harry.salary)

