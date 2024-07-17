# write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if(a>b):
    if(a>c):
        if(a>d):
            print(a, "is a lagest number")
        else:
            print(d, "is a lagest number")
    else:
        if(c>d):
            print(c, "is a lagest number")
        else:
            print(d, "is a lagest number")
else:
    if(b>c):
        if(b>d):
            print(b, "is a lagest number")
        else:
            print(d, "is a lagest number")
    else:
        if(c>d):
            print(c, "is a lagest number")
        else:
            print(d, "is a lagest number")

        

if(a>b and a>c and a>d):
    print("Greatest number is a:",a)

elif(b>a and b>c and b>d):
    print("Greatest number is b:",b)

elif(c>b and c>a and c>d):
    print("Greatest number is c:",c)

if(d>b and d>c and d>a):
    print("Greatest number is d:",d)    


    