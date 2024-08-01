'''
 Create a class "programmer" for storing information of few programmers 
 working at microsoft.
'''

class programmer:
    company = "microsoft"
    def __init__(self, name, eID, salary):
        self.salary = salary
        self.name = name
        self.eID = eID

    def empDetials(self):
        print(f"The company name is {self.company}. Name is {self.name}. eID is {self.eID}. Salary is {self.salary}")

p = programmer("priyanka" , 224126, 1300000)
# print(p.company, p.name, p.salary , p.eID)
p.empDetials()         

s = programmer("sandip" , 224127, 1200000)
# print(s.company, s.name, s.salary , s.eID)
s.empDetials()        