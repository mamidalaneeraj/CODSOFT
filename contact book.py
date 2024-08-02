print('Welcome to the Contact Book')
print('---------------------------')

# Creating a class ContactBook
class ContactBook:
    def __init__(self):
        self.contacts = {}

    # Function to add contact
    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter the address: ").strip()
        if name and phone and email and address:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print("Contact added successfully!")
        else:
            print("All fields are required to add a contact.")

    # Function to view contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, details in self.contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")
                print(f"Address: {details['address']}")
                print("------------------------")

    # Function to search contact
    def search_contact(self):
        name = input("Enter name to search: ").strip()
        if name in self.contacts:
            details = self.contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
        else:
            print("Contact not found!")

    # Function to delete contact
    def delete_contact(self):
        name = input("Enter name to delete: ").strip()
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Function to update contact
    def update_contact(self):
        name = input("Enter name to update: ").strip()
        if name in self.contacts:
            phone = input("Enter new phone number: ").strip()
            email = input("Enter new email: ").strip()
            address = input("Enter new address: ").strip()
            if phone and email and address:
                self.contacts[name] = {"phone": phone, "email": email, "address": address}
                print("Contact updated successfully!")
            else:
                print("All fields are required to update a contact.")
        else:
            print("Contact not found!")

# Main function
def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.delete_contact()
        elif choice == '5':
            contact_book.update_contact()
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
