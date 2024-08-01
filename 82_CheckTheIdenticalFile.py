with open("text.txt", "r") as file:
    content = file.read()

with open("text1.txt", "r") as file:
    content1 = file.read()

if(content == content1):
    print("Yes these files are identical")

else:
    print("No these files are identical")