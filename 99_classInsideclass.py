'''
Create a class 'Pets' from a class 'Animals' and further create a class 
'Dog' from 'pets'. Add a method 'bark to class 'Dog'.
'''

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bhau-bhau")

tommy = Dog()

tommy.bark()
