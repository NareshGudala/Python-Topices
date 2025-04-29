"""
INHERITANCE

-> single
-> multilevel
-> multiple
-> Hierarchial

"""

"""single"""
# class parent():
#     def fun(self):
#         print("i am parent")
# class child(parent):
#     def func(self):
#         print("i am child")
# c = child()
# c.func()  # child method
# c.fun()   # parent method    


"""Multilevel"""

# class Grandparent():
#     def fun1(self):
#         print("i am Grandparent")
# class parent(Grandparent):
#     def fun(self):
#         print("i am parent")
# class child(parent):
#     def func(self):
#         print("i am child")
# c = child()
# c.func()  # child method
# c.fun()   # parent method      
# c.fun1()  # Grandparent method 

"""multiple"""

# class Father():
#     def fun1(self):
#         print("i am Father")
# class Mother():
#     def fun(self):
#         print("i am Mother")
# class child(Father,Mother):
#     def func(self):
#         print("i am child")
# c = child()
# c.fun1()  # child method
# c.fun()   # parent method      
# c.func()

"""Hierachical"""

class Father():
    def fun1(self):
        print("i am Father")
class child1(Father):
    def fun(self):
        print("i am child1")
class child2(Father):
    def func(self):
        print("i am child2")
c1 = child1()
c2 = child2()
c1.fun()
c1.fun1()
c2.func()
c2.fun1()
