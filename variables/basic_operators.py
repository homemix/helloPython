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
tuple = ('ken', 455, 'joy', 'emmah', 67)
print(tuple)
# tuple[0]='kennedy'

""" Dictionary"""
print(" ++++++++++++++++++")
print("PYTHON DICTIONARY \n")
dict = {}
dict['name'] = 'kennedy'
dict['age'] = '37'
dict['class'] = 'python'
print(dict)
print(dict.keys())
print(dict.values())
dict['age'] = 56
print(dict)

""" Basic Operators"""
print(" ++++++++++++++++++\n")
print("PYTHON OPERATORS ")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is y)
print(x is z)

""" Membership operators (in, not in)"""
print("banana" in x)

""" Core data types"""
print(" ++++++++++++++++++\n")
print("PYTHON CORE OPERATORS ")

f = open('data.txt', 'w')
f.write("hello python\n")

f.close()

# sets
thisest = {"apple","banana","cherry"}
print(thisest)
names=["kennedy","ken","judy","faith"]
newset= set(names)
print(newset)

# Numbers
a= 5
print(a,"is of type",type(a))

