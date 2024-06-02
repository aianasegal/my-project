from enum import Enum

contacts = []

class Actions(Enum):
    ADD = 1
    EXIT = 5

def menu():
    print("Menu:")
    print("1. Add Contact")
    print("5. Exit")

def add():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == Actions.ADD.value:
                add()
            elif choice == Actions.EXIT.value:
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Please enter a valid option.")
        else:
            print("Invalid choice! Please enter a valid option.")
quit


