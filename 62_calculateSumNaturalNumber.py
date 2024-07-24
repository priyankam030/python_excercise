# Write a recursive function to calculate the sum of first n natural number

# def natural_num(n):
#     return(n*(n+1)/2)

# n = int(input("Enter a number: "))
# num = natural_num(n)
# print(f"Natural number is: {num}")

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4....n-1 + n
sum(n) = sum(n-1) + n
'''

def natural_num(n):
    if (n==1):
        return 1
    num = natural_num(n-1) + n
    return num

n = int(input("Enter a number: "))

print(natural_num(n))