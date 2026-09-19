# Menu-driven List CRUD Operations

my_list = ["Apple", "Banana", "Cherry"]

def show_menu():
    print("\n--- List Menu ---")
    print("1. Add item")
    print("2. Display list")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        item = input("Enter item to add: ")
        my_list.append(item)
        print("Added!")
    elif choice == '2':
        print("\nCurrent list:", my_list)
    elif choice == '3':
        index = int(input("Enter index to update: "))
        if 0 <= index < len(my_list):
            new_item = input("Enter new value: ")
            my_list[index] = new_item
            print("Updated!")
        else:
            print("Invalid index.")
    elif choice == '4':
        index = int(input("Enter index to delete: "))
        if 0 <= index < len(my_list):
            my_list.pop(index)
            print("Deleted!")
        else:
            print("Invalid index.")
    elif choice == '5':
        break
    else:
        print("Invalid choice, try again.")
