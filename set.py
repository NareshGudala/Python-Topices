"""
SET

-> { }
-> do not allow duplicate
-> do index unoredered
-> do not allow mutable types as set elements

 """

# a = {12,25,45,78,15,75,89,101}
# print("SET")
# print(a)
# print(type(a))

"""
SET method

-> add()
-> update()
-> pop()
-> remove()
"""

# print("\n")
# print("add")
# a.add(121)
# print(a)

# print("\n")
# print("update")
# a.update({1,2,3,4})
# print(a)

# print("\n")
# print("pop")
# a.pop()
# print(a)

# b = {1,2,3,4,5,6,7,8,9}
# print("\n")
# print("remove")
# b.remove(9)
# print(b)

"""
SET operation

-> union()
-> intersection()
-> difference()
-> issubset()
-> issuperset()

"""
# print("\n")
# print("Union")
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7}
# print(s1.union(s2))

# print("\n")
# print("Intersection")
# print(s1.intersection(s2))

# print("\n")
# print("difference")
# print(s2.difference(s1))


set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8}
print("\n")
print("issubset")
print(set2.issubset(set1))

print("\n")
print("issuperset")
print(set1.issuperset(set2))