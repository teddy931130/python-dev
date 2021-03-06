import sys
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
8. Exit
    """)


def search_by_name(db):
    contacts = db

    first_name = input("Enter contact's first name: ")
    first_names = [x.first_name for x in contacts]
    if first_name in first_names:
        last_name = input("Enter contact's last name: ")
        last_names = [x.last_name for x in contacts]
        if last_name in last_names:
            pass
        else:
            print(f'\nNo last name "{last_name}" for contact "{first_name}" in the database!\n')
            input('Press "Enter" to return to main menu...')
            return
    else:
        print(f'\nNo first name "{first_name}" in the database!\n')
        input('Press "Enter" to return to main menu...')
        return

    name = f"{first_name} {last_name}"
    for contact in contacts:
        if name == f"{contact.first_name} {contact.last_name}":
            print(f"\n{name}")
            print("=" * len(name))
            print(f" - Number:\t{contact.number}")
            print(f" - City:\t{contact.city}\n")


def search_by_city(db):
    contacts = db

    city_input = input("Enter contact's city: ")
    cities = [x.city for x in contacts]
    if city_input in cities:
        for contact in contacts:
            if contact.city == city_input:
                name = f"{contact.first_name} {contact.last_name}"

                print(f"\n{name}")
                print("=" * len(name))
                print(f" - Number:\t{contact.number}")
                print(f" - City:\t{contact.city}\n")

        input(f'\nPress "Enter" to return to main menu...')
    else:
        print(f'\nA contact from city "{city_input}" does not exist!\n')
        input('Press "Enter" to return to main menu...')


def search_by_number(db):
    contacts = db

    number_input = input("Enter contact's number: ")
    numbers = [x.number for x in contacts]
    if number_input in numbers:
        for contact in contacts:
            if contact.number == number_input:
                name = f"{contact.first_name} {contact.last_name}"

                print(f"\n{name}")
                print("=" * len(name))
                print(f" - Number:\t{contact.number}")
                print(f" - City:\t{contact.city}\n")

        input('\nPress "Enter" to return to main menu...')
    else:
        print(f'\nA contact with number "{number_input}" does not exist!\n')
        input('Press "Enter" to return to main menu...')


def show_all(db):
    contacts = db

    if contacts:
        for contact in contacts:
            name = f"{contact.first_name} {contact.last_name}"
            print(name)
            print("=" * len(name))

            print(f" - Number:\t{contact.number}")
            print(f" - City:\t{contact.city}\n")
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

    first_name = input("Enter first name: ")
    first_names = [x.first_name for x in contacts]
    if first_name in first_names:
        last_name = input("Enter last name: ")
        last_names = [x.last_name for x in contacts]
        if last_name in last_names:
            pass
        else:
            print(f'\nNo last name "{last_name}" for contact "{first_name}" in the database!\n')
            input('Press "Enter" to return to main menu...')
            return
    else:
        print(f'\nNo first name "{first_name}" in the database!\n')
        input('Press "Enter" to return to main menu...')
        return

    name = f"{first_name} {last_name}"
    number = input("Enter number: ")
    city = input("Enter city: ")

    for line in fileinput.input("database.txt", inplace=True):
        args = f'Contact("{first_name}", "{last_name}", "{number}", "{city}")'
        temp = line.split(" - ")[1]
        temp = temp.split("(")[1]
        temp = " ".join(temp.split(", ")[:2]).replace('"', '')

        if temp == name:
            temp = f'{line.split(" - ")[0]} - {args}\n'
            sys.stdout.write(temp)
        else:
            sys.stdout.write(line)

    print("\nContact updated successfully!\n")
    input("Press enter to return to main menu...")


def delete_contact(db):
    contacts = db
    first_name = input("Enter first name: ")
    first_names = [x.first_name for x in contacts]
    if first_name in first_names:
        last_name = input("Enter last name: ")
        last_names = [x.last_name for x in contacts]
        if last_name in last_names:
            pass
        else:
            print(f'\nNo last name "{last_name}" for contact "{first_name}" in the database!\n')
            input('Press "Enter" to return to main menu...')
            return
    else:
        print(f'\nNo first name "{first_name}" in the database!\n')
        input('Press "Enter" to return to main menu...')
        return

    delete_user = f"{first_name} {last_name}"
    found = False

    for contact in contacts:
        if delete_user == f"{contact.first_name} {contact.last_name}":
            found = True
            break

    if found:
        with open("database.txt", "r") as file:
            lines = file.readlines()

        with open("database.txt", "w") as file:
            for line in lines:
                if first_name not in line and last_name not in line:
                    file.write(line)

        print("\nUser deleted successfully!\n")
        input('Press "Enter" to return to main menu...')
    else:
        print("\nNo such user in the database!\n")
        input('Press "Enter" to return to main menu...')
        return


def exit_app():
    exit(0)


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
    elif value == "8":
        print("""
========
GOODBYE!
========
""")
        exit_app()


if __name__ == "__main__":
    while True:
        database = open_database()

        usage()
        user_input = input("Select option [1 - 8]: ")
        choices = ["1", "2", "3", "4", "5", "6", "7", "8"]

        if user_input not in choices:
            print("\nInvalid input! Please, try again.")
        else:
            choice(user_input, database)
