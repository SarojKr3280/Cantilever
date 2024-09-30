# PROJECT 1

def display_menu():
    print("\n----- CONTACT BOOK -----")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def view_contacts():
    with open("contacts.txt", 'r') as file:
        contacts = file.readlines()

        if contacts:
            print("\n----- Contacts -----")
            for idx, contact in enumerate(contacts, start=1):
                print(f"{idx}. {contact.strip()}")

        else:
            print("\nNo Contacts Available")


def add_contact():
    name = input("\nEnter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    email = input("Enter the email of the contact: ")

    contact_info = f"name: {name} | Phone: {phone} | Email: {email}\n"

    with open("contacts.txt", 'a') as file:
        file.write(contact_info)

    print(f"Contact: {name} added !!!")


def search_contact():
    keyword = input("\nEnter a keyword to search the contact: ")

    with open("contacts.txt", 'r') as file:
        contacts = file.readlines()

    matched_contact = [contact.strip() for contact in contacts if keyword.lower() in contact.lower()]

    if matched_contact:
        print("\n----- MATCHED CONTACTS -----")
        for idx, contact in enumerate(matched_contact, start=1):
            print(f"{idx}. {contact}")
    else:
        print("Contact Not Found")


def delete_contact():
    view_contacts()

    number = int(input("\nEnter the contact serial number to delete: "))
    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()

        if 1 <= number <= len(contacts):
            deleted_contact = contacts.pop(number)

            with open('contacts.txt', 'w') as file1:
                file1.writelines(contacts)

            print(f"Contact: {deleted_contact.strip()} deleted !!! ")
        else:
            print("Invalid Contact Serial Number. Please enter correct contact serial number. ")
