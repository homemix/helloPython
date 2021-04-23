import os
import pickle

try:
    # fileobject = open("app.log", encoding='utf-8')
    # fileobject = open('content/testfile.txt','a')
    # fileobject.write("Now the file has more content than before!")

    fileobject = open('content/testfile.txt','w')
    fileobject.write("Woops! I have deleted the contents in there by accident!")


    # print(fileobject.read())
    # print(fileobject.readline())
    # print('File name: ', fileobject.name)
    # print(' opening mode: ',fileobject.mode)
finally:
    fileobject.close()

file = open('content/presidents.txt','r+')
# file.seek(2)
# print(file.readline())
# print(file.tell())

file.close()

# with open('content/presidents.txt', 'r') as reader:
#     print(reader.read())

pets_dict = [{ 'Bob': 13,
              'Jimmy': 2,
              'Laika': 3,
              'Jimmy': 10,
              'Jack': 3,
              'Stella': 3,
              'Nzinga': 7 },
]
pickle.dump(pets_dict,open('pets.txt','ab'))
pets = pickle.load(open('pets.txt','rb'))
print(pets)