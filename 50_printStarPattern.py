# write a program to print the following star pattern.
'''
       *
     * * *
   * * * * *
   '''

# for j in range (3):
#     for i in range(1, 6):
#         if (i == 3):
#             print("*")
#         else:
#             print(" ")

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")

