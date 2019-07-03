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
            value = line.split(" | ")[1]  # some fine tuning for the
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


def search_name(db):
    pass


def search_city(db):
    pass


def search_number(db):
    pass


def show_all(db):
    contacts = db
    for contact, info in contacts.items():
        print()
        print(contact)
        print("="*len(contact))
        info = list(info.items())

        for each in info:
            print(f" - {each[0]}:\t{each[1]}")

    print()
    input("Press enter to return to main menu...")


def add_contact(db):
    contacts = db
    name = input("Enter name: ")
    # check if name is already in database
    if name in contacts.keys():
        print("Contact already exists! Use option 7 to update contact.")
        input("Press enter to return to main menu...")
    else:
        number = input("Enter number: ")
        city = input("Enter city: ")
        info = {
            "name": name,
            "number": number,
            "city": city,
        }

        contacts[name] = info

        with open("database.txt", "a+") as file:
            line = f"{name} | name: {info['name']}, number: {info['number']}, city: {info['city']}\n"
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
        search_name(users)
    elif value == "2":
        print()
        print("==============")
        print("SEARCH BY CITY")
        print("==============")
        search_city(users)
    elif value == "3":
        print()
        print("================")
        print("SEARCH BY NUMBER")
        print("================")
        search_number(users)
    elif value == "4":
        print()
        print("=================")
        print("SHOW ALL CONTACTS")
        print("=================")
        show_all(users)
    elif value == "5":
        print()
        print("===============")
        print("ADD NEW CONTACT")
        print("===============")
        add_contact(users)
    elif value == "6":
        print()
        print("=======================")
        print("UPDATE EXISTING CONTACT")
        print("=======================")
        update_contact(users)
    elif value == "7":
        print()
        print("==============")
        print("DELETE CONTACT")
        print("==============")
        delete_contact(users)


if __name__ == "__main__":
    while True:
        database = open_database()

        usage()
        user_input = input("Select option[1 - 7]: ")
        choices = ["1", "2", "3", "4", "5", "6", "7"]

        if user_input not in choices:
            print("Invalid input!")
            print()
        else:
            choice(user_input, database)
