# Write a python function to remove a given word from a list and strip it at the same time.



def removeWord(list , member):
        list.remove(member)
        return list

list_1 = ["Mohit", "Radhika", "Rohan", "Prashu", "Shubh"]

list_2 = removeWord(list_1, "Mohit")

print(list_2)