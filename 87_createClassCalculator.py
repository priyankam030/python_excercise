'''
 Write a class "calculator" capable of finding squre cude squre root of 
 a number.
'''
class claculator:
    def __init__(self, n):
        self.n = n
    def squre(self):
        print(f"The squre is {self.n * self.n}")
    def cube(self):
        print(f"The cube is {self.n * self.n *self.n}")
    def squreroot(self):
        print(f"The squreroot is {self.n **(1/2)}")


a = claculator(4)
a.squre()
a.cube()
a.squreroot()