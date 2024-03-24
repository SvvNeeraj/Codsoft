class Contact:
    def __init__(self, name, phone_no, email, address):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for index, contact in enumerate(self.contacts):
            print(f"{index + 1}. {contact.name} - {contact.phone_no}")

    def search_contact(self, search_query):
        found_contacts = []
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower() or search_query in contact.phone_no:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, updated_contact):
        self.contacts[index] = updated_contact

    def delete_contact(self, index):
        del self.contacts[index]

def display_menu():
    print("****Contact Book****")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
def add_contact_menu(contact_manager):
    name = input("Enter name: ")
    phone_no = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = Contact(name, phone_no, email, address)
    contact_manager.add_contact(contact)
    print("Contact added successfully!")


def view_contacts_menu(contact_manager):
    contact_manager.view_contacts()

def search_contact_menu(contact_manager):
    search_query = input("Enter name or phone number to search: ")
    found_contacts = contact_manager.search_contact(search_query)
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"{contact.name} - {contact.phone_no}")
    else:
        print("No contacts found.")


def update_contact_menu(contact_manager):
    index = int(input("Enter index of contact to update: ")) - 1
    if 0 <= index < len(contact_manager.contacts):
        name = input("Enter updated name: ")
        phone_no= input("Enter updated phone number: ")
        email = input("Enter updated email: ")
        address = input("Enter updated address: ")
        updated_contact = Contact(name,phone_no, email, address)
        contact_manager.update_contact(index, updated_contact)
        print("Contact updated successfully!")
    else:
        print("Invalid index.")


def delete_contact_menu(contact_manager):
    index = int(input("Enter index of contact to delete: ")) - 1
    if 0 <= index < len(contact_manager.contacts):
        contact_manager.delete_contact(index)
        print("Contact deleted successfully!")
    else:
        print("Invalid index.")


def main():
    contact_manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact_menu(contact_manager)
        elif choice == '2':
            view_contacts_menu(contact_manager)
        elif choice == '3':
            search_contact_menu(contact_manager)
        elif choice == '4':
            update_contact_menu(contact_manager)
        elif choice == '5':
            delete_contact_menu(contact_manager)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

 