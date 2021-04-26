import ast
import json
import pickle
from os import path

filename = "contacts.txt"

contacts = []


def create_contact(phone_key=None):
    first_name = input("Enter first name:")
    middle_name = input("Enter middle name:")
    last_name = input("Enter last name:")
    address = input("Enter mailing address:")
    email = input("Enter the email:")
    if phone_key is not None:
        phone = phone_key
    else:
        phone = input("Enter the phone number:")
    city = input("Enter the city:")
    country = input("Enter the country:")
    zipcode = input("Enter the zipcode:")
    full_name = first_name + " " + middle_name + " " + last_name
    new_contact = {'full_name': full_name,
                   'address': address,
                   'email': email,
                   'city': city,
                   "phone": phone,
                   'country': country,
                   'zipcode': zipcode}
    contacts_dict = {
        phone: new_contact
    }

    if path.exists(filename):
        with open(filename, 'rb') as read_file:
            contacts_from_file = pickle.load(read_file)
            if phone_key is not None:
                contacts_from_file[phone_key] = new_contact
            else:
                contacts_from_file[phone] = new_contact

        with open(filename, 'wb') as handle:
            pickle.dump(contacts_from_file, handle)
        print("Contact added/updated successfully")
    else:
        with open(filename, 'wb') as handle:
            pickle.dump(contacts_dict, handle)
            print("Contact created successfully")


def read_contacts(phone_read=None):
    data = pickle.load(open(filename, 'rb'))
    if phone_read is not None:
        print(data.get(phone_read))
    else:
        for key, value in data.items():
            print(key, value)


def close_program():
    exit("The program is closed.")


def delete_contact(phone_delete):
    with open(filename, 'rb') as read_file:
        contacts_from_file = pickle.load(read_file)
        if phone_delete is not None:
            del contacts_from_file[phone_delete]

    with open(filename, 'wb') as handle:
        pickle.dump(contacts_from_file, handle)
    print(phone_delete + " was deleted successfully")


print(" 1. List Phone Numbers\n 2. Add a Contact \n 3. Remove a Contact")
print(" 4. Update a Contact\n 5. Look up a contact by Number")
print(" Q. Quit")
option = input("Type a number (1-5 or Q):")

if option == '1':
    read_contacts()
elif option == '2':
    create_contact()
elif option == '3':
    number = input("enter phone number to delete:")
    delete_contact(number)
elif option == '4':
    number = input("enter phone number to Update:")
    create_contact(number)
elif option == '5':
    number = input("enter phone number to Search:")
    read_contacts(number)
elif option == 'Q':
    close_program()
else:
    print("Invalid Option")
