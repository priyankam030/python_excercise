'''
use static method to print greet "hello world" 
'''
class Greet:
    def Greet(self):
        print("hello world")

    @staticmethod
    def greet():
        print("hello world")

a = Greet()

a.greet()
a.Greet()