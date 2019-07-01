def open_database():
    contacts = {}
    with open("database.txt", "r") as file:
        # File structure: Georgi | name: Georgi, age: 25, city: Sofia
        # remove \n from end of each line in the file
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
    Select option[1 - 5]:
    1. Search by name
    2. Search by city
    3. Search by number
    4. Show all contacts
    5. Add new contact
    6. Delete contact
    7. Update contact
    """)


def search_name(database):
    name = input("Enter name: ")




def search_city(database):
    pass


def search_number(database):
    pass


def show_all(database):
    pass


def add_contact(database):
    name = input("Enter name: ")
    number = input("Enter number: ")
    city = input("Enter city: ")
    entry = {
        "name": name,
        "number": number,
        "city": city,
    }


    print("New contact added successfully!")
    print("Press enter to return to main menu...")



def delete_contact(database):
    pass


def update_contact(database):
    pass


def choice(value, db):
    value = int(value)
    if value == 1:
        search_name(db)
    elif value == 2:
        search_city(db)
    elif value == 3:
        search_number(db)
    elif value == 4:
        show_all(db)
    elif value == 5:
        add_contact(db)
    elif value == 6:
        delete_contact(db)
    elif value == 7:
        update_contact(db)





if __name__ == "__main__":

    while True:
        # with open("database.txt", "w+") as file:
        #     file = dict(file)
        user_input = int(input("Select option[1 - 5]: "))
        usage()
        if not 1 <= user_input <= 7:
            print("Invalid input!")
            print()
        else:
            choice(user_input, file)
