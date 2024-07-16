s = {1, 4, 5, 67, 8, "Priyanka", 46}

print(s, type(s))

s.add(344)

print(s, type(s))

s1 = s.__len__()
print(s1)

# s2 = s.remove(4)
# print(s2)
 

# s.clear()
# print(s, type(s))

s3 = s.union({67,6})

print(s, type(s))

s4 = s.intersection({8, 67, 5, 4, 3})

print(s4, type(s))