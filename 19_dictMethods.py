marks = {
    "Harry" : 100, 
    "Shubham" : 56,
    "Rohan" : 23
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99 , "renuka": 100})
print(marks)
print(marks.get("Rohan"))
print(marks["Rohan"])

# print(marks.get("Rohan1")) # it will return none.
# print(marks["Rohan1"]) # key error.


marks.clear()

print(marks)






