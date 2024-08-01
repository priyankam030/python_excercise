class Employee:
    # language = "py" # This is a class attribute
    # salary = 1300000

    def __init__(self, Name, Salary, Language): # dunder method which is automatically called
        self.name = Name
        self.salary = Salary
        self.language = Language
        print("I am creating an object")

        
    def getInfo(self):
        print(f"Name is {self.name}. The language is {self.language}. The salary is {self.salary}")


harry = Employee("Harry", 1200000, "Javascript")  # create object 
# print(harry.name, harry.salary, harry.language)  
harry.name = "Sandip"
# print(harry.name, harry.salary, harry.language)
harry.getInfo()

