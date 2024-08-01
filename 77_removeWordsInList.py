# Repeat privious question for a list of such words to be censored.

words = ["fool", "non", "animal"]

file = open("words.txt", "r")

read = file.read()
print(read)
file.close()

for word in words:
    read = read.replace(word, "#" * len(word) )

with open ("words.txt", "w") as file:
    print(read)
    file.write(read)
