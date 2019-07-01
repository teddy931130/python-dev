def open_database():
    contacts = {}
    with open("database.txt", "a+") as file:
        # go to beginning of file since a+ goes to the end
        # we do a+ because we want to create the database.txt if it doesn't exist
        file.seek(0)
        # File structure: Georgi | name: Georgi, age: 25, city: Sofia
        # remove \n from end of each line in the file
        lines = file.read().splitlines()

        # get left and right part for the entry
        for line in lines:
            key = line.split(" | ")[0]
            value = line.split(" | ")[1][:-1]
            value = value.split(",")

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
1. Search by name
2. Search by city
3. Search by number
4. Show all contacts
5. Add new contact
6. Delete contact
7. Update contact
    """)


def search_name(db):
    name = input("Enter name: ")


def search_city(db):
    pass


def search_number(db):
    pass


def show_all(db):
    contacts = db
    for contact, info in contacts.items():
        print()
        print(contact)
        print("========")
        info = list(info.items())

        for each in info:
            print(f" - {each[0]}:\t{each[1]}")


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
            file.write(f"{name} | ")

            info = list(info.items())
            for key, value in info:
                file.write(f"{key}: {value},")
            file.write("\n")


        print()
        print("New contact added successfully!")
        input("Press enter to return to main menu...")


def delete_contact(db):
    pass


def update_contact(db):
    pass


def choice(value, db):
    value = int(value)
    users = db
    if value == 1:
        search_name(users)
    elif value == 2:
        search_city(users)
    elif value == 3:
        search_number(users)
    elif value == 4:
        show_all(users)
    elif value == 5:
        add_contact(users)
    elif value == 6:
        delete_contact(users)
    elif value == 7:
        update_contact(users)


if __name__ == "__main__":

    while True:

        database = open_database()

        usage()
        user_input = int(input("Select option[1 - 7]: "))

        if not 1 <= user_input <= 7:
            print("Invalid input!")
            print()
        else:
            choice(user_input, database)
