import os
import sys


def restart_program():
    os.execv(sys.executable, [sys.executable] + sys.argv)


region = input("Select your Region: A- for African, O- for other:")
if region == 'O':
    exit("The scholarship is only for Africans. Thanks for your interest")
elif region != 'A':
    print('Invalid choice: select A for African or O for other')
    restart_program()

student_name = input("Enter Student Name:")
student_gender = input("Enter student Gender (F-female, M- Male):")
student_id = input("Enter Student ID:")
student_address = input("Enter Student Mailing address:")
student_email = input("Enter Student Email:")
student_phone = input("Enter Student Phone number:")
quizes = input("Enter quiz1,quiz2,quiz3 separated by comma:")
quiz_list = quizes.split(',')
quiz_avg = (float(quiz_list[0]) + float(quiz_list[1]) + float(quiz_list[2])) / len(quiz_list)

tests = input("Enter Test1,Test2 separated by commas:")
test_list = tests.split(',')
test_avg = (float(test_list[0]) + float(test_list[1])) / len(test_list)

zoom_points = input("Enter the zoom call score [0-9]:")
homework = input("Enter Home work score max=10:")

print("_____________STUDENT DETAILS______________")
print("Student Name: " + student_name)
print('Student ID: ' + student_id)
print('Gender: ' + student_gender)
print('Phone: ' + student_phone)
print('Address: ' + student_address)
print('Quiz Score: ' + str(quiz_avg))
print('Zoom calls Score: ' + zoom_points)
print('Test Score: ' + str(test_avg))
print('Homework Score: ' + homework)
if quiz_avg >= 80 and student_gender == 'M':
    print('Qualified For Scholarship')
elif quiz_avg >= 76 and student_gender == 'F':
    print('Qualified For Scholarship')
else:
    print('Thanks for trying: Not qualified')
