# python: Add two given lists using map and lambda

l1 = [1,2,3]
l2 = [3,4,5]

print("Original list")
print(l1)
print(l2)
result = map(lambda x, y:x+y,l1,l2)
print("result:")
print(list(result))