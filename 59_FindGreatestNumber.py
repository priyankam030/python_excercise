# Write a program using function of find greatest of three numbers.

def greatest_num(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c 
    
# greatest_num = int(input("Enter a number: "))
a = 2
b = 14
c = 7

print(greatest_num(a, b ,c))