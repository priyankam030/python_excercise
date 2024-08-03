class number:
    def __init__(self, n):
        self.n = n
        

    def __add__(self, obj):
        return self.n + obj.n
    

val1 = number(5)
print(val1.n)

val2 = number(2)
print(val2.n)


# print(val1.__add__(val2))
print(val1 + val2)