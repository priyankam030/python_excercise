''' A file contain a word "donkey" multiple times. You need to write a 
program which replace this word with ##### by updating the same file. '''

string = "######" 

f = open("words.txt" , "r")
r = f.read()
f.close()

newWord = r.replace(string, "He")

with open ("words.txt", "w") as f:
    f.write(newWord)
