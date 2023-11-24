class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter the contact name: ")
        phone = input("Enter the contact phone number: ")
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}")

    def search_contacts(self):
        keyword = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if keyword.lower() in (contact.name.lower(), contact.phone.lower())]
        if found_contacts:
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self):
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(self.contacts):
            name = input("Enter the updated name: ")
            phone = input("Enter the updated phone number: ")
            self.contacts[index].name = name
            self.contacts[index].phone = phone
            print("Contact updated successfully!")
        else:
            print("Invalid index.")

    def delete_contact(self):
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid index.")


if __name__ == "__main__":
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contacts()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
