import models.Contacts
import models.Search
import models.FileIO

class AddressBook:
    def __init__(self):
        # A dictionary of address book maintained. 'default' will be the default address book
        self.address_book = {'default': []}
        # Creating an instance of Search class
        self.search_obj = models.Search.Search()
        # Creating an instance of File object
        self.file = models.FileIO.FIleIO()


    # method to add a contact to address book
    def add_contact(self, contact, ab_name):
        self.address_book[ab_name].append(contact)
        
        self.push_to_file(contact, ab_name)
        self.save_to_csv(ab_name)
        self.save_to_json(ab_name)



    # Pushing data into a text file
    def push_to_file(self, contact, ab_name):
        self.file.write_contact_to_file(contact, ab_name)

    def save_to_csv(self, ab_name):
        self.file.save_to_csv(self.address_book[ab_name], ab_name)

    def save_to_json(self, ab_name):
        self.file.save_to_json(self.address_book[ab_name], ab_name)
        


    # method to get contact info from user and adds it to address book
    def get_info(self, ab_name):
        f_name = input("First Name: ")
        l_name = input("Last Name: ")

        # Checks if ciontact with same first and last name exists
        if any(c.f_name == f_name and c.l_name == l_name for c in self.address_book[ab_name]):
            print("Contact with this name already exists.")
            return

        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        new_contact = models.Contacts.Contact(f_name, l_name, city, state, zip_code, phone, email)

        self.search_obj.update_city_state_dict(f_name, city, state)
        self.add_contact(new_contact, ab_name)
        self.push_to_file(new_contact, ab_name)

    # Method to display contacts
    def display_contacts(self, ab_name):
        if not self.address_book[ab_name]:
            print("Address book is empty.")
            return

        for contact in self.address_book[ab_name]:
            print("Contact Details:")
            print(f"first name: {contact.f_name},\n last name: {contact.l_name},\n city: {contact.city},\n state: {contact.state},\n zip code: {contact.zip_code},\nphone number: {contact.phone},\nemail: {contact.email}")
            print()
    
    # Method to find contact by first name or last name
    def findByName(self, name, ab_name):
        for index, contact in enumerate(self.address_book[ab_name]):
            if contact.f_name == name or contact.l_name == name:
                return index
        return None

    # Method to edit person details if person exists
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

    # Method to add multiple adddress books. Adds another key to address_book dictionary
    def add_multiple_address_books(self):
        n = int(input("How many address book you need to add?: "))  
        for _ in range(n):
            ab_name = input("Enter the name of the new address book: ")
            if(ab_name in self.address_book):
                print("Address book with this name already exists.")
            else:
                self.address_book[ab_name] = []
                print(f"Address book '{ab_name}' added successfully.")

    def search_person_by_city(self):
        city_name = input("Enter city name: ")
        self.search_obj.search_by_city(city_name)

    def search_by_state(self):
        state_name = input("Enter state name: ")
        self.search_obj.search_by_state(state_name)

    def get_count_by_city(self):
        city_name = input("Enter city name: ")
        count = self.search_obj.get_person_count(city_name)
        print(f"Number of persons in city '{city_name}': {count}")

    def get_count_by_state(self):
        state_name = input("Enter state name: ")
        count = self.search_obj.get_person_count_state(state_name)
        print(f"Number of persons in state '{state_name}': {count}")

    def sort_by_name(self, current_ab, option):
        option_list = ['f_name', 'city', 'state', 'zip_code']
        print(f"Sorting by {option_list[option - 1]}")
        self.address_book[current_ab].sort(key = lambda contact : contact.__getattribute__(option_list[option - 1]))
        self.display_contacts(current_ab)
           

