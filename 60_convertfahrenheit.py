# Write a python program using function to convert celsius to fahrenheit


def fahrenheit(n):
    return (n * 9/5) + 32

n = int(input("Enter temperature (in celsius)  : "))

print(f"The number is in {fahrenheit (n)} degree celsius")