from contact_functions import *
import os

if os.path.isfile("contacts.txt"):
    pass
else:
    file = open('contacts.txt', 'x')


while True:
    display_menu()
    choice = int(input("\nEnter your choice (1-5): "))

    match choice:
        case 1:
            view_contacts()
        case 2:
            add_contact()
        case 3:
            search_contact()
        case 4:
            delete_contact()
        case 5:
            print("Exited the program. Namaste !!!")
            break
        case _:
            print("! Invalid choice !\n Please enter correct choice.")
