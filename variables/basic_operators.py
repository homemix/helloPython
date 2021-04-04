mystring = "hello"
myfloat = 10.0
myint = 20

# testing the code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float:%f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer:%d" % myint)

""" Standard Data Types"""
str = 'Hello World!'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)

""" Lists"""
print(" ++++++++++++++++++")
print("PYTHON LISTS \n")
list = ['mango', 'guava', 'avocado', '23', 'kennedy']
print(list)
print(list[-1])
list.append(1)
print(list)

for x in list:
    print(x)

""" Tuples"""
print(" ++++++++++++++++++")
print("PYTHON TUPLES \n")

