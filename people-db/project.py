import sys
import os
import fileinput


class Contact:
    def __init__(self, first_name, last_name, number, city):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.city = city

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def open_database():
    contacts = []
    with open("database.txt", "a+") as file:
        # go to beginning of file since a+ goes to the end
        # we do a+ because we want to create the database.txt if it doesn't exist
        file.seek(0)

        # File structure: Contact("Ivan Peshev", "0865648", "Sofia")
        # remove \n from end of each line in the file with splitlines()

        lines = file.read().splitlines()

        for line in lines:
            new_contact = eval(line.split(" - ")[1])
            contacts.append(new_contact)

    return contacts


def usage():
    print("""
==========
|| MENU ||
==========
1. Search by name
2. Search by city
3. Search by number
4. Show all contacts
5. Add new contact
6. Update contact
7. Delete contact
    """)


def search_by_name(db):
    contacts = db
    name_input = input("Enter contact's name: ")

    for name, info in contacts.items():
        if info["name"] == name_input:
            print()
            print(name_input)
            print("=" * len(name_input))
            info = list(info.items())

            for each in info:
                print(f" - {each[0]}:\t{each[1]}")

            print()
            input("Press enter to return to main menu...")
            return

    print()
    print(f"Contact {name_input} does not exist!")
    print()
    search_by_name(contacts)


def search_by_city(db):
    contacts = db
    city_input = input("Enter contact's city: ")
    cities = []

    for name, info in contacts.items():
        cities.append(info["city"])

    if city_input in cities:
        for name, info in contacts.items():
            if info["city"] == city_input:
                print()
                print(info["name"])
                print("=" * len(info["name"]))
                info = list(info.items())

                for each in info:
                    print(f" - {each[0]}:\t{each[1]}")

        print()
        input("Press enter to return to main menu...")
    else:
        print()
        print(f"A contact from {city_input} does not exist!")
        print()
        search_by_city(contacts)


def search_by_number(db):
    contacts = db
    number_input = input("Enter contact's number: ")
    numbers = []

    for name, info in contacts.items():
        numbers.append(info["number"])

    if number_input in numbers:
        for name, info in contacts.items():
            if info["number"] == number_input:
                print()
                print(info["name"])
                print("=" * len(info["name"]))
                info = list(info.items())

                for each in info:
                    print(f" - {each[0]}:\t{each[1]}")
                break
        print()
        input("Press enter to return to main menu...")
    else:
        print()
        print(f"A contact with number {number_input} does not exist!")
        print()
        search_by_number(contacts)


def show_all(db):
    contacts = db

    if contacts:
        for contact in contacts:
            name = f"{contact.first_name} {contact.last_name}"
            print(name)
            print("=" * len(name))

            print(f" - Number:\t{contact.number}")
            print(f" - City:\t{contact.city}")
            print()
    else:
        print("There are no contacts in the database!")
        return

    input('Press "Enter" to return to main menu...')


def add_contact(db):
    contacts = db
    exists = False

    with open("database.txt", "r+") as file:
        lines = file.read().splitlines()
        if lines:
            last_id = int(lines[-1].split(" - ")[0])
        else:
            last_id = 0

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    number = input("Enter number: ")
    city = input("Enter city: ")

    args = f'Contact("{first_name}", "{last_name}", "{number}", "{city}")'
    current_contact = eval(args)
    for contact in contacts:
        if current_contact == contact:
            print("\nA contact with identical attributes already exists!")
            input('Press "Enter" to return to main menu...')
            exists = True
            break

    if not exists:
        with open("database.txt", "a+") as file:
            line = f'{last_id + 1} - Contact("{first_name}", "{last_name}", "{number}", "{city}")\n'
            file.write(line)

    print("\nNew contact added successfully!\n")
    input('Press "Enter" to return to main menu...')


def update_contact(db):
    contacts = db

    name = input("Enter name: ")
    number = input("Enter number: ")
    city = input("Enter city: ")

    info = {
        "name": name,
        "number": number,
        "city": city,
    }

    contacts[name] = info

    for line in fileinput.input("database.txt", inplace=True):
        temp = line.split(" | ")[0]
        if temp.split(" - ")[1] == name:
            temp = f"{temp.split(' - ')[0]} - {name} | name: {info['name']}, number: {info['number']}, city: {info['city']}\n"
            sys.stdout.write(temp)
        else:
            sys.stdout.write(line)

    print()
    print("Contact updated successfully!")
    input("Press enter to return to main menu...")


def delete_contact(db):
    contacts = db
    delete_user = input("User to delete: ")
    found = False

    for key, value in contacts.items():
        if delete_user == key.split(" - ")[1]:
            found = True
            break

    if found:
        with open("database.txt", "r") as file:
            lines = file.readlines()

        with open("database.txt", "w") as file:
            for line in lines:
                if delete_user not in line:
                    file.write(line)

        print("User deleted successfully!")
        input("Press enter to return to main menu...")
    else:
        print("No such user in the database!")
        delete_contact(contacts)


def choice(value, db):
    users = db
    if value == "1":
        print("""
==============
SEARCH BY NAME
==============
""")
        search_by_name(users)
    elif value == "2":
        print("""
==============
SEARCH BY CITY
==============
""")
        search_by_city(users)
    elif value == "3":
        print("""
================
SEARCH BY NUMBER
================
""")
        search_by_number(users)
    elif value == "4":
        print("""
=================
SHOW ALL CONTACTS
=================
""")
        show_all(users)
    elif value == "5":
        print("""
===============
ADD NEW CONTACT
===============
""")
        add_contact(users)
    elif value == "6":
        print("""
=======================
UPDATE EXISTING CONTACT
=======================
""")
        update_contact(users)
    elif value == "7":
        print("""
==============
DELETE CONTACT
==============
""")
        delete_contact(users)


if __name__ == "__main__":
    while True:
        database = open_database()

        usage()
        user_input = input("Select option [1 - 7]: ")
        choices = ["1", "2", "3", "4", "5", "6", "7"]

        if user_input not in choices:
            print("\nInvalid input! Please, try again.")
        else:
            choice(user_input, database)
