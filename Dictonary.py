"""
--> { }
--> key, value data(k:v)
--> key should be immutable
--> key will act as index
--> no slicing
--> keys are unquie

"""
print("Dictonary")
a = {'book_id' : 501, "college_id" : 401, 1 : "Aditya Engineering College"}
print(a)
print(type(a))

# print("\n")
# print("Index")
# print(a[1])

"""
Dictornary Methods

-> get()
-> update()
-> values()
-> keys()
-> items()

"""
print("\n")
print("get method")
print(a.get(1))

print("\n")
print("Keys method")
print(a.keys())

print("\n")
print("values method")
print(a.values())

print("\n")
print("items method")
print(a.items())

print("\n")
print("update method")
a.update({12 : "Sony"})
print(a)


"""
for loop in dict
calling keys & values

"""

print("\n")
print("using For in dictonary : ")
for i,j in a.items():
    print(i,j)