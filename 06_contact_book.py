# Contact Book Using a Dictionary

contacts = {}

def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added!")
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated!")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
