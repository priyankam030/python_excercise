''' Write a program to read the text from a given file
 'poems.txt' and find out whether it contains the word 'priyanka'.
'''

poemFile = open("poems.txt")

poem = poemFile.read()

if ("priyanka" in poem):
    print("The word is present in poem")
else:
    print("The word is not present in poem")


poemFile.close()