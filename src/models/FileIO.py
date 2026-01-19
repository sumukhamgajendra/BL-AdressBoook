class FIleIO:


    def write_contact_to_file(self, contact, ab_name):
        name = f"{ab_name}_address_book.txt"
        with open(f"C:\\Users\\LENOVO\\OneDrive - PESUNIVERSITY\\Desktop\\Sumukha\\Stud\\Python\\Python-practice\\Python-BL-Projects\\AddressBook\\src\\Files\\{name}", "a") as file:
            file.write(f"{contact.f_name},{contact.l_name},{contact.city},{contact.state},{contact.zip_code},{contact.phone},{contact.email}\n")

   