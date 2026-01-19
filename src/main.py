import models.Addressbook

class Main:
    @staticmethod
    def start():
        address_book_main = models.Addressbook.AddressBook()
        while True:
            print("Address Book")
            print("What operation you need to perform?: \n1.Add a contact \n2.Display contacts\n3.edit contact\n4.Exit")

            choice = int(input("Enter your choice: "))
            print()

            match choice:

                case 1:
                    print("Add a new contact")
                    address_book_main.get_info()

                case 2:
                    address_book_main.display_contacts()

                case 3:
                    name = input("Enter the name of the person to edit: ")
                    pos = address_book_main.findByName(name)
                    if pos is not None:
                        address_book_main.edit_person(pos)
                    else:
                        print("No contacts found")
                case 4:
                    break

if __name__ == "__main__":
    Main.start()