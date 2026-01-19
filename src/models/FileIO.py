class FIleIO:


    def write_contact_to_file(self, contact, ab_name):
        name = f"{ab_name}_address_book.txt"
        with open(f"C:\\Users\\LENOVO\\OneDrive - PESUNIVERSITY\\Desktop\\Sumukha\\Stud\\Python\\Python-practice\\Python-BL-Projects\\AddressBook\\src\\Files\\{name}", "a") as file:
            file.write(f"{contact.f_name},{contact.l_name},{contact.city},{contact.state},{contact.zip_code},{contact.phone},{contact.email}\n")

    def save_to_csv(self, address_book, ab_name):
        if ab_name not in address_book:
            print("No contacts to save.")
            return
        import csv
        with open(f"{ab_name}_address_book.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'City', 'State', 'Zip Code', 'Phone Number', 'Email'])
            for contact in address_book:
                writer.writerow([contact.f_name, contact.l_name, contact.city, contact.state, contact.zip_code, contact.phone, contact.email])
    
    def save_to_json(self, address_book, ab_name):
        if ab_name not in address_book:
            print("No contacts to save.")
            return
        import json
        data = []
        for contact in address_book:
            data.append(contact.to_dict())
        with open(f"{ab_name}_address_book.json", "w") as file:
            json.dump(data, file, indent=4)