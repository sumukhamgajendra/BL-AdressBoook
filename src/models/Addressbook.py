import models.Contacts

class AddressBook:
    def __init__(self):
        self.address_book = {'default': []}

    def add_contact(self, contact):
        self.address_book['default'].append(contact)

    def get_info(self):
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        new_contact = models.Contacts.Contact(f_name, l_name, city, state, zip_code, phone, email)
        self.add_contact(new_contact)

    def display_contacts(self):
        if not self.address_book['default']:
            print("Address book is empty.")
            return

        for contact in self.address_book['default']:
            print("Contact Details:")
            print(f"first name: {contact.f_name},\n last name: {contact.l_name},\n city: {contact.city},\n state: {contact.state},\n zip code: {contact.zip_code},\nphone number: {contact.phone},\nemail: {contact.email}")
            print()
    
    def findByName(self, name):
        for index, contact in enumerate(self.address_book['default']):
            if contact.f_name == name or contact.l_name == name:
                return index
        return None
    
    def edit_person(self, pos):
        contact = self.address_book['default'][pos]
        print("Editing contact. Press enter to keep current value.")

        contact.f_name = input("Enter new First Name: ") or contact.f_name
        contact.l_name = input("Enter new Last Name: ") or contact.l_name
        contact.city = input("Enter new City: ") or contact.city
        contact.state = input("Enter new State: ") or contact.state
        contact.zip_code = int(input("Enter new Zip Code: ")) or contact.zip_code
        contact.phone = int(input("Enter new Phone Number: ")) or contact.phone
        contact.email = input("Enter new Email: ") or contact.email
        print("Contact updated successfully.")