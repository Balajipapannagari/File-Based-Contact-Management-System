import csv
import os

FILE_NAME = "contacts.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])


def get_valid_email():
    while True:
        email = input("Enter email : ")
        if email.lower().endswith("@gmail.com"):
            return email
        else:
            print(" Invalid email!, please enter the correct email. ")


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = get_valid_email()

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print(" Contact added successfully!")


def view_contacts():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        contacts = list(reader)

        if len(contacts) <= 1:
            print(" No contacts found.")
            return

        print("\n--- Contact List ---")
        for row in contacts[1:]:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")


def search_contact():
    keyword = input("Enter name or phone to search: ")

    found = False
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if keyword.lower() in row[0].lower() or keyword in row[1]:
                print(f" Found: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                found = True

    if not found:
        print(" Contact not found.")


def update_contact():
    phone_to_update = input("Enter phone number of contact to update: ")
    updated_contacts = []
    updated = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_contacts.append(header)

        for row in reader:
            if row[1] == phone_to_update:
                print("Enter new details:")
                name = input("New name: ")
                phone = input("New phone: ")
                email = get_valid_email()
                updated_contacts.append([name, phone, email])
                updated = True
            else:
                updated_contacts.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_contacts)
        print(" Contact updated successfully!")
    else:
        print(" Contact not found.")


def delete_contact():
    phone_to_delete = input("Enter phone number to delete: ")
    updated_contacts = []
    deleted = False

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)
        updated_contacts.append(header)

        for row in reader:
            if row[1] == phone_to_delete:
                deleted = True
            else:
                updated_contacts.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_contacts)
        print(" Contact deleted successfully!")
    else:
        print(" Contact not found.")


def main():
    initialize_file()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(" Exiting program.")
            break
        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
