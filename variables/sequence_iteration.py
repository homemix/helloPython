
#name = input("Enter your name")
#print("hello "+ name)

""" IF Statements\n"""
flag = False
if flag:
    print("welcome ")
    print(" to python class")

number = 300
if number < 500:
    print("number is less than 500")

if number %2 ==0:
    print("Even number")
    if -999 >= number:
        print("two digit negative number")
else:
    print("odd number")

if 9 < number < 99:
    print("two digit number")
elif 99 < number < 999:
    print("three digit number")
elif 999 < number < 9999:
    print("four digit number")
else:
    print("greater than five digit number")

    """ Iteration Loops"""
print("++++++++++++++++\n")
print("PYTHON ITERATION")

numbers = [1,2,4,7,9,34,78,23]
sq =0
for val in numbers:
    sq = val*val
    #print(sq)

fruits = ["Lemon", "apple", "banana", "Avocado", "cherry","Papaya"]
# for spelling in "banana":
#      print(spelling)

for fruit in fruits:
    if fruit =="Avocado":
        continue
    print(fruit)

for fruit in range(3,10,2):
    print(fruit)
else:
    print("finally done")

adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for describe in adjective:
    for name in fruits:
        print(describe,name)

index =0
while index <6:
    index+=1
    if index == 3:
        continue
    print(index)
else:
    print("index is no longer less than 6")