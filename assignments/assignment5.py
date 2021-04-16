import os
import sys


def print_options():
    print("Options:")
    print("[P] Print Options")
    print("[C] Convert from Celsius")
    print("[F] Convert from Fahrenheit")
    print("[NM] Convert from Nautical Miles")
    print("[KM] Convert from Kilometers")
    print("[In] Convert from Inches")
    print("[CM] Convert from Centimeters")
    print("[M] Convert from Meters")
    print("[Y] Convert from Yards")
    print("[Q] Quit")


def temperature(from_input, value):
    if from_input == 'F':
        temp_c = ((value - 32) * (5 / 9))
        return "Fahrenheit temperature: " + str(from_input) + "\n Celsius:" + str(temp_c)
    elif from_input=='C':
        temp_f = (value * 1.8) + 32
        return "Celsius temperature: " + str(from_input) + "\n Fahrenheit:" + str(temp_f)
    else:
        return "Invalid temperature Key"


def distance(from_input, value):
    if from_input == 'NM':
        km = (value / 0.53996)
        return "Nautical Miles: " + str(value) + "\n Kilometers:" + str(km)
    elif from_input == 'KM':
        nm = value * 0.6214
        return "Kilometers: " + str(value) + "\n Nautical Miles:" + str(nm)
    elif from_input == 'In':
        cm = (value / 0.39370)
        return "Inches: " + str(value) + "\n Centimeters:" + str(cm)
    elif from_input == 'CM':
        inches = (value * 0.39370)
        return "Centimeters: " + str(value) + "\n Inches:" + str(inches)
    elif from_input == 'M':
        yards = (value * 1.0936)
        return "Meters: " + str(value) + "\n Yards:" + str(yards)
    elif from_input == 'Y':
        meters = (value * 1.0936)
        return "Yards: " + str(value) + "\n Meters:" + str(meters)
    else:
        return "invalid option"


def close_program():
    exit()


def restart_program():
    os.execv(sys.executable, [sys.executable] + sys.argv)


print(print_options())
print("Enter the option")
option = (input())
if option == 'Q':
    close_program()
print("Enter the value")
values = int(input())

if option == 'F' or option == 'C':
    print(temperature(option, values))
elif option == 'NM' or option == 'KM' or option == 'In' or option == 'CM' or option == 'M' or option == 'Y':
    print(distance(option, values))
elif option == 'Q':
    close_program()
elif option == 'P':
    print_options()
else:
    print("Invalid option, Select Valid Option")
    restart_program()
