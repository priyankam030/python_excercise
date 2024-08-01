with open ("text.txt", "r") as file:
    Content = file.read()
print(Content)

with open ("text1.txt", "w") as file:
    file.write(Content)
    # print(Content)

    