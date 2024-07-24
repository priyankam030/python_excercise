# Write a python function to print first n lines of the following pattern
'''
***
**
*
'''

def star(n):
    if(n==0):
       return
    print("*" * n)
    star(n-1)

star(3)
    