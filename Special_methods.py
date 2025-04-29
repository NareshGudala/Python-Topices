'''
Special methods - [also magic methods or dunder methods, because of they start and end with double underscore,__]

'''
#  * __int__ [constructor] : called when an object is created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person.name)  # Output: Alice
print(person.age)   # Output: 25
