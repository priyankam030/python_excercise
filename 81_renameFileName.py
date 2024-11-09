'''
Write a python program to rename a file to 'old.txt'
'''

import os

with open("old.txt", "r") as file:
    content = file.read()
    print(content)

with open("new.txt", "w") as file:
    file.write(content)

os.remove("old.txt")