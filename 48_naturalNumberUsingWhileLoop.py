# write a program to find the sum of first n natural numbers using while loop
# Farmula  S = n(n+1)/2
#
n = int(input("Enter a number: "))

sum = 0
i = 1
while(i <= n):
    sum = sum + i
    i += 1
print(f"Sum of {n} number is {sum}")   



    
 