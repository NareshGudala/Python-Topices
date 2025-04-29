"""
FUNCTION

-> block of a code
-> run when its called

syntax:

 keyword 
 ^
 |
----
def function.name():  ==} function defination
-----------------------
     function body
-----------------------
function.name()       ==} function calls

"""

def add(a,b):
    return a+b
print(add(45,54))

def func(a,b):                          # function defination
    print("function numbers are :",a,b) # function body
func(210,420)                           # function call


# Nested Function

# print("\n")
# print("nested function")
# def outer():
#     print("outer")
#     def inner():
#         print("inner")
#     inner()
# outer()        

# def fun(*n):
#     print("Hi", n)
# fun(1,2,3)    



def num(a,b):
    def sub(c,d):
        return c-d
    print(sub(36,12))
    return a+b
print(num(12,36))
