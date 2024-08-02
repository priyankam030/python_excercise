'''
when a child class becomes a parent for another child class.
          parent =   child1  +  child2

'''
class Employee:
    a = 1
class programmer(Employee):
    b = 2
class manager(programmer):
    c =3

o = Employee()
print(o.a) # Print the a attribute
# print(o.b) # Show an error as there is no b attribute in employee class

o = programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)

           
