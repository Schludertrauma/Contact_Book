'''contact_book.py'''
'''This script defines a ContactBook that manages a collection of contacts.'''
'''It allows adding, removing, retrieving and viewing contacts by name.'''
'''This script is only a cli_tool for exercising basic file operations and data management.'''


# ContactBook class definition and library imports


import sys
import time


class ContactBook:
    def welcome(self):
        # Display a welcome message and instructions
        print("Welcome to the Contact Book!")
        time.sleep(1.5)
        print("You can add, remove, change, and view contacts by name.")
        time.sleep(1.5)

    def exit(self):
        # Display exit message and terminate the program
        print("Exiting the Contact Book. Goodbye!")
        time.sleep(1.5)
        sys.exit()

    def save(self):
        # check for txt file and save contacts
        with open('contacts.txt', 'w') as file:
            for name, phone in self.contacts.items():
                file.write(f"{name}: {phone}\n")
        print("Contacts saved to contacts.txt")
        time.sleep(1.5)

    def load_contacts(self):
        # Load contacts from a file if it exists
        try:
            with open('contacts.txt', 'r') as file:
                for line in file:
                    name, phone = line.strip().split(': ')
                    self.contacts[name] = phone
            print("Contacts loaded from contacts.txt")
        except FileNotFoundError:
            print("No contacts file found. Starting with an empty contact book.")
        except Exception as e:
            print(f"An error occurred while loading contacts: {e}")

    def manage_contacts(self):
        # Main loop to manage contacts
        self.contacts = {}
        self.load_contacts()
        self.welcome()

        while True:
            print("\nOptions: add, remove, change, view, exit")
            choice = input("Choose an option: ").strip().lower()

            if choice == 'add':
                name = input("Enter contact name: ").strip()
                phone = input("Enter contact phone number: ").strip()
                self.contacts[name] = phone
                print(f"Contact {name} added.")
                self.save()

            elif choice == 'remove':
                name = input("Enter contact name to remove: ").strip()
                if name in self.contacts:
                    del self.contacts[name]
                    print(f"Contact {name} removed.")
                    self.save()
                else:
                    print(f"Contact {name} not found.")

            elif choice == 'change':
                name = input("Enter contact name to change: ").strip()
                if name in self.contacts:
                    new_phone = input("Enter new phone number: ").strip()
                    self.contacts[name] = new_phone
                    print(f"Contact {name} updated.")
                    self.save()
                else:
                    print(f"Contact {name} not found.")

            elif choice == 'view':
                name = input(
                    "Enter contact name to view or enter 'all': ").strip()
                if name == 'all':
                    for contact_name, phone in self.contacts.items():
                        print(f"{contact_name}: {phone}")
                elif name in self.contacts:
                    print(f"{name}: {self.contacts[name]}")
                else:
                    print(f"Contact {name} not found.")

            elif choice == 'exit':
                self.exit()

            else:
                print("Invalid option. Please try again.")


# Main execution block to run the ContactBook application


if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.manage_contacts()
