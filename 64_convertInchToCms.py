# Write a python function which converts inches to cms.
# Farmula inch = 2.54 cm

def value(n):
    a = n * 2.54
    return(a)

n = int(input("Enter a number: "))
ans = value(n)
print(f"The corresponding value is in cms = {ans}cm")