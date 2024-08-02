"""
Create a class with a class attribute a; create an object from it and 
set 'a' directly using object.a = o.Does this change the class attribute?
"""
class Class:
   a =  1

b = Class()
print(b.a) # Print the class attribute because instance attribute is not present.
b.a = 0 # Instance attribute is set.
print(b.a) # Print the instance attribute because instance attribute is present.
print(Class.a) # This does not change the class attribute.
