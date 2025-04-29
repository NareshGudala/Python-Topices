"""
TUPLE

-> ()
-> Allow different types of elemnts
-> Allow duplicates
-> Allow index & slicing
-> Immutable
-> No methods we can use bulti-in
"""

# t = (1,3,5,8,12)
# print("tuple")
# print(t)

"""
-> sum
-> minimum
-> maximum
-> length

"""

# print("sum")
# print(sum(t))
# print("minimum")
# print(min(t))
# print("maximum")
# print(max(t))
# print("length")
# print(len(t))

"""
--> Concatenation
--> Iteration
--> Repetation
--> Membership operation
--> Identify operation
"""

# print("\n")

# print("Concatenation")
t1 = (1,2,3)
t2 = (7,8,9)
# print(t1+t2)


# print('\n')
# print("Repetation")
# print(t1*2)

# print('\n')
# print("Iteration")
# for i in t1:
#     print(i)


# print('\n')
# print("Membership")
# print(1 in t1)    
# print(t1 is t2)
# print(4 is not t2)

# print("\n")



#================ ATM==================
name="nans"
password="123"
user_name=input("Enter the user Name:")
Password=input("Enter the password:")
s = '''
    1.Credit
    2.Debit
    3.Mini statement
    4.Exit
    
    '''

Amount = 1000
if name==user_name and password==Password:
    while True:
        print(s)
        option=int(input("Enter the option:"))
        if option==1:
            credit_amount=float(input("Enter the Amount:"))
            print("Amount after credits:", Amount + credit_amount)
        elif option==2:
            debit_amount=float(input("Enter the Amount:"))
            print("Amount after debit:",Amount - debit_amount)
        elif option==3:
            print("Amount:",Amount) 
        elif option==4:
            break     
else:
    print("Incorrect")           