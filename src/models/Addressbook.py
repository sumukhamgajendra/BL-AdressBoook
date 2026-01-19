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