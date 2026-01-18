import models.Addressbook

class Main:
    @staticmethod
    def start():
        address_book_main = models.Addressbook.AddressBook()
        while True:
            print("Address Book")
            print("What operation you need to perform?: \n1.Add a contact \n2.Display contacts\n3.exit")

            choice = int(input("Enter your choice: "))
            print()

            match choice:

                case 1:
                    print("Add a new contact")
                    print("Add a new contact")
                    address_book_main.get_info()

                case 2:
                    address_book_main.display_contacts()

                case 3:
                    print("Exiting the Address Book application.")  
                    break

if __name__ == "__main__":
    Main.start()