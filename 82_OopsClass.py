class Employee:
    language = "py" # This is a class attribute
    salary = 1300000

harry = Employee()
harry.name = "harry" # This is an instance (object) attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan maurya"
print(rohan.name, rohan.salary, rohan.language)


''' 
Here name is instance (object) attribute and salary and language are class
attributes as they directly belong to the class
'''