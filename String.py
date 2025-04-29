"""
STRING  --> Collection of characters

Declaring String
single Quote --> (' ')
Double Quote --> (" ")
Triple Quote --> ('''   ''')

"""

# print('Naresh')
# print("Nans")
# print('''Nani''')
# print(type('Nani'))

"""
String methods

upper()
lower()
startswith()
endswith()
count()
removeprefix()
removesuffix()
split()
replace()
strip()
rstrip()
lstrip()
index()
find()
"""

# a = "Welcome KPHB"
# print(a.upper())

# b = "Welcome KPHB"
# print(b.lower())

# c = "Welcome KPHB"
# print(c.startswith('W'))

# d = "Welcome KPHB"
# print(d.endswith('a'))

# e = "Welcome to KPHB"
# print(e.replace('KPHB','Telegana'))

# f = "Welcome to Telegana"
# print(f.count('e'))

# g = "Welcome to Telegana"
# print(g.find('W'))
# print(g.index('Telegana'))

h = "  Welcome to Telegana  "
print(h)
# c = "Welcome to KPHB"
# print(h.removeprefix("Telegana"))
# print(h.removesuffix("telegana"))

print(h.strip())
# print(len(h))
# print(c)

print(h.rstrip())
print(h.lstrip())
