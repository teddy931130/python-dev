import sys
import fileinput


def open_database():
    contacts = {}
    with open("database.txt", "a+") as file:
        # go to beginning of file since a+ goes to the end
        # we do a+ because we want to create the database.txt if it doesn't exist
        file.seek(0)

        # File structure: Georgi | name: Georgi, age: 25, city: Sofia
        # remove \n from end of each line in the file with splitlines()

        lines = file.read().splitlines()

        # get left and right part for the entry
        for line in lines:
            key = line.split(" | ")[0]
            value = line.split(" | ")[1]
            value = value.split(", ")

            info = {}
            # get left and right part for the info of the entry
            for each in value:
                x = each.split(": ")[0]
                y = each.split(": ")[1]
                info[x] = y

            # update the contacts with the entry
            contacts[key] = info
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

    if name_input in contacts:
        for name, info in contacts.items():
            if name == name_input:
                print()
                print(name)
                print("=" * len(name))
                info = list(info.items())

                for each in info:
                    print(f" - {each[0]}:\t{each[1]}")

        print()
        input("Press enter to return to main menu...")
    else:
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
                print(name)
                print("=" * len(name))
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
                print(name)
                print("=" * len(name))
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

    for name, info in contacts.items():
        print(name.split(" - ")[1])
        print("="*len(name.split(" - ")[1]))
        info = list(info.items())

        for each in info:
            print(f" - {each[0]}:\t{each[1]}")
        print()

    print()
    input("Press enter to return to main menu...")


def add_contact(db):
    contacts = db
    exists = False

    with open("database.txt", "r+") as file:
        lines = file.read().splitlines()
        last_id = int(lines[-1].split(" - ")[0])

    name = input("Enter name: ")
    number = input("Enter number: ")
    city = input("Enter city: ")

    for contact, values in contacts.items():
        if name == contact.split(" - ")[1]:
            if number == values["number"]:
                if city == values["city"]:
                    print()
                    print("A contact with those attributes already exists!")
                    input("Press enter to return to main menu...")
                    exists = True

    if not exists:
        info = {
            "name": name,
            "number": number,
            "city": city,
        }

        contacts[f"{last_id + 1} - {name}"] = info

        with open("database.txt", "a+") as file:
            line = f"{last_id + 1} - {name} | name: {info['name']}, number: {info['number']}, city: {info['city']}\n"
            file.write(line)

        print()
        print("New contact added successfully!")
        input("Press enter to return to main menu...")


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
        if line.strip().startswith(name):
            line = f"{name} | name: {info['name']}, number: {info['number']}, city: {info['city']}\n"
        sys.stdout.write(line)

    print()
    print("Contact updated successfully!")
    input("Press enter to return to main menu...")


def delete_contact(db):
    contacts = db
    delete_user = input("User to delete: ")

    if delete_user in contacts.keys():
        with open("database.txt", "r") as file:
            lines = file.readlines()

        with open("database.txt", "w") as file:
            for line in lines:
                if delete_user not in line:
                    file.write(line)

        input()
        print("User deleted successfully!")
        input("Press enter to return to main menu...")
    else:
        print("No such user in the database!")
        delete_contact(contacts)


def choice(value, db):
    users = db
    if value == "1":
        print()
        print("==============")
        print("SEARCH BY NAME")
        print("==============")
        print()
        search_by_name(users)
    elif value == "2":
        print()
        print("==============")
        print("SEARCH BY CITY")
        print("==============")
        print()
        search_by_city(users)
    elif value == "3":
        print()
        print("================")
        print("SEARCH BY NUMBER")
        print("================")
        print()
        search_by_number(users)
    elif value == "4":
        print()
        print("=================")
        print("SHOW ALL CONTACTS")
        print("=================")
        print()
        show_all(users)
    elif value == "5":
        print()
        print("===============")
        print("ADD NEW CONTACT")
        print("===============")
        print()
        add_contact(users)
    elif value == "6":
        print()
        print("=======================")
        print("UPDATE EXISTING CONTACT")
        print("=======================")
        print()
        update_contact(users)
    elif value == "7":
        print()
        print("==============")
        print("DELETE CONTACT")
        print("==============")
        print()
        delete_contact(users)


if __name__ == "__main__":
    while True:
        database = open_database()

        usage()
        user_input = input("Select option[1 - 7]: ")
        choices = ["1", "2", "3", "4", "5", "6", "7"]

        if user_input not in choices:
            print("Invalid option!")
            print()
        else:
            choice(user_input, database)
