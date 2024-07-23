# write a program to print multipication table of n using by for loop in reversed order.


n = int(input("Enter a number: "))
# i = 10 
for i in range(1, 11):
    print(f"{n} x {11-i} = {n*(11-i)}")