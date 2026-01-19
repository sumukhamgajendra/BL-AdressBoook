import models.Contacts

class AddressBook:
    def __init__(self):
        self.address_book = {'default': []}

    def add_contact(self, contact, ab_name):
        self.address_book[ab_name].append(contact)

    def get_info(self, ab_name):
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        new_contact = models.Contacts.Contact(f_name, l_name, city, state, zip_code, phone, email)
        self.add_contact(new_contact, ab_name)

    def display_contacts(self, ab_name):
        if not self.address_book[ab_name]:
            print("Address book is empty.")
            return

        for contact in self.address_book[ab_name]:
            print("Contact Details:")
            print(f"first name: {contact.f_name},\n last name: {contact.l_name},\n city: {contact.city},\n state: {contact.state},\n zip code: {contact.zip_code},\nphone number: {contact.phone},\nemail: {contact.email}")
            print()
    
    def findByName(self, name, ab_name):
        for index, contact in enumerate(self.address_book[ab_name]):
            if contact.f_name == name or contact.l_name == name:
                return index
        return None

    def edit_person(self, pos, ab_name):
        contact = self.address_book[ab_name][pos]
        print("Editing contact. Press enter to keep current value.")

        contact.f_name = input("Enter new First Name: ") or contact.f_name
        contact.l_name = input("Enter new Last Name: ") or contact.l_name
        contact.city = input("Enter new City: ") or contact.city
        contact.state = input("Enter new State: ") or contact.state
        contact.zip_code = int(input("Enter new Zip Code: ")) or contact.zip_code
        contact.phone = int(input("Enter new Phone Number: ")) or contact.phone
        contact.email = input("Enter new Email: ") or contact.email
        print("Contact updated successfully.")

    
    def add_multiple_address_books(self):
        n = int(input("How many address book you need to add?: "))  
        for _ in range(n):
            ab_name = input("Enter the name of the new address book: ")
            if(ab_name in self.address_book):
                print("Address book with this name already exists.")
            else:
                self.address_book[ab_name] = []
                print(f"Address book '{ab_name}' added successfully.")
