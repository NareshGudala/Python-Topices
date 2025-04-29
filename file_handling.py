'''
files handling

=> Reading, writing, deleting, creating of a file is called file handling.

open  ==> open()
read/write
close ==> close()


  MODES
r -> read
w -> write [Truncate]
a -> append
r+ -> read,write
w+ -> write,read[Truncate]

'''
# s = open('demo.txt' ,mode ='r')
# print(s.read())


# f = open("demo.txt", mode="r+")
# print(f.read())
# f.write("bye.. 420 ")
# f.close()

# w = open("demo.txt",mode = 'a')
# # print(w.write())
# w.write("hi")
# w.close()

# # Reading file in 'r+' mode:
# with open('demo.txt','r+') as fd:
#     print(fd.tell())
#     print(fd.read())
#     print(fd.tell())



# # Read file in  'w+' mode:
# with open('demo.txt',mode='w+') as fd:
#     print(fd.tell())
#     c=fd.write("This is write & read")
#     print(fd.read())
#     print(fd.tell())


# # write file in 'r+' mode
# with open('demo.txt','r+') as fd:
#     fd.write("New text.")



# with open('sample1.txt','r+') as fd:
#     pass
# # opening file in 'w+' mode when it does not exist
# with open('sample1.txt','w+') as fd:
#     pass

'''

tell() method can be used to get the position of file handle.
tell() method returns current position of file object.
This method takes no parameters and returns an integer value.

'''

'''

seek() function is used to change the position of the file handle 
to a given specific position.
File handle is like a cursor, which defines from where the data has
to be read or written in the file.

'''