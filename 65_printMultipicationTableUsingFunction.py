# Write a python function to print multipication table of a given number.

def table(n):
    for i in range (1, 11):
        ans = n * i
        print(ans)
    return

n = int(input("Enter a number: "))   
table(n)
    