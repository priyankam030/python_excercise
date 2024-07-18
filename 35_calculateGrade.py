# write a program to calculate the grade of a student from his marks from the following scheme.
# 90 to 100 => Ex
# 80 to 90 => A
# 70 to 80 => B
# 60 to 70 => C
# 50 to 60 => D
# <90 => F

marks = int(input("Enter your marks: "))

if(marks <= 100 and marks >= 90):
    print("Your grade is Ex")

elif(marks <= 90 and marks >= 80):
    print("Your grade is A")

elif(marks <= 80 and marks >= 70):
    print("Your grade is B")

elif(marks <= 70 and marks >= 60):
    print("Your grade is C")

elif(marks <= 60 and marks >= 50):
    print("Your grade is D")

elif(marks < 50 and marks > 0):
    print("Your grade is F")


else:
    print("Invalid number")
