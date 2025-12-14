import json
import os

FILE_NAME = "contacts.json"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump({}, file, indent=4)

def load_contacts():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ").strip()

    if name in contacts:
        print("❌ Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("✅ Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("📭 No contacts found.")
        return

    print("\n📒 Contact List:")
    for name, info in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("-" * 30)

def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ").strip()

    if name in contacts:
        info = contacts[name]
        print("\n🔍 Contact Found")
        print(f"Name : {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("❌ Contact not found!")

def update_contact():
    contacts = load_contacts()
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("❌ Contact does not exist!")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("✅ Contact updated successfully!")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found!")

def menu():
    print("\n📘 Contact Book Application")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    initialize_file()
    while True:
        menu()
        choice = input("Choose an option (1-6): ").strip()

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
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
