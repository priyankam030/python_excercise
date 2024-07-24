# Write a python program using function to convert celsius to fahrenheit


def fahrenheit(n):
    fahrenheit_val = ((n * 9/5) + 32)
    return fahrenheit_val

n = int(input("Enter temperature (in celsius)  : "))
temp = fahrenheit (n)
print(f"The number is in {temp} degree celsius")