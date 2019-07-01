
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


if __name__ == "__main__":
    database = open_database()
    input("Press enter to return to main menu...")
    # print(database)

