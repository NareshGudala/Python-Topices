# write a python program to detect the number of local variable in the functio.

# local variable --> inside function
# global variable --> outside fuction


str="naresh"  # Global Variable
def nans():
    x=2
    y=3
    n="Nans"
    f=2.2
print(nans.__code__.co_nlocals)    