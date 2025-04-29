# def poly(a,b):
#     c = a+b
#     print(c)
# poly(12,23)
# poly([1,2],[2,6])
# poly('Nar','esh')


#===========LIBRARY MANGEMENT===========

print("    SOSO LIBRARY      ")
user="nans"
password="@123"
Username=input("Enter the Library User Name:")
Password=input("Enter the Library Password:")

library = '''
    1.Login 
    2.Author
    3.Book Name
        a.c
        b.c++
        c.Python
    4.Logout

    '''
Author = ['Naresh','Balaji','Nani','Antony']

if user==Username and password==Password:
    while True:
        print(library)
        option=input("Enter the option:")
        if option==1:
            print("Login Successfully")
        # elif option==2:
        #     Author_name=input("Enter the Author Name:")
        #     break
else:
    print("Incorrect")           
                
