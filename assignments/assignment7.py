import ast
import json
import pickle


def create_contact():
    first_name = input("Enter first name:")
    middle_name = input("Enter middle name:")
    last_name = input("Enter last name:")
    address = input("Enter mailing address:")
    email = input("Enter the email:")
    phone = input("Enter the phone number:")
    city = input("Enter the city:")
    country = input("Enter the country:")
    zipcode = input("Enter the zipcode:")
    full_name = first_name + " " + middle_name + " " + last_name
    contacts = {'full_name': full_name,
                'address': address,
                'email': email,
                'city': city,
                'country': country,
                'zipcode': zipcode}

    pickle.dump(contacts, open('contacts/contacts.txt', 'ab'))


def read_contacts():
    data = pickle.load(open('contacts/contacts.txt', 'rb'))
    print(data)


# def delete_contact(phone):
#     with open('contacts/contacts.txt', 'r') as file:
#         contact_list = file.read()
#         if phone in contact_list:
#             contact_list.

# print(create_contact())
print(read_contacts())
