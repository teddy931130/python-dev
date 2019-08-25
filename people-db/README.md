Program Structure
=================

1 - FUNCTIONS:

- open_database() --> Generates a list of objects from database.txt
- usage() --> Print main menu / program usage
- search_by_name() --> Search a contact by his name
- search_by_city() --> Search a contact by his city
- search_by_number() --> Search a contact by his number
- show_all() --> Show all contacts in the database 
- add_contact() --> Add a new contact
- update_contact() --> Update an existing contact's info
- delete_contact() --> Delete a contact
- choice() --> Perform action based on user's choice


2 - DATABASE:

- A simple "database.txt" file in current process directory 


3 - DATABASE STRUCTURE:

example line: 1 - Teodor | name: Teodor, number: 123, city: Sofia

             \_/  \____/  \______________________________/
              |     |                     |
             id   contact             attributes
