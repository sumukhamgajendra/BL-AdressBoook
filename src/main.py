import models.Addressbook

class Main:
    @staticmethod
    def start():
        address_book_main = models.Addressbook.AddressBook()
        current_ab = 'default'
        while True:
            print(f"--------'{current_ab}' Address Book--------")
            print("What operation you need to perform?: \n1.Add a contact \n2.Display contacts\n3.edit contact\n4.Delete contact\n5.Add multiple contacts\n6.Add multiple address books\n7.Switch address book\n8.search person by city or state\n9.To count By city or state\n10.sort by name\n11.Exit")

            choice = int(input("Enter your choice: "))
            print()

            match choice:
                # case 1 adds new contact to specified address book
                case 1:
                    print("Add a new contact")
                    address_book_main.get_info(current_ab)

                # case 2 displays all contacts in specified address book
                case 2:
                    address_book_main.display_contacts(current_ab)

                # case 3 checks if person with name exists and edits contact if exists in specified address book
                case 3:
                    name = input("Enter the name of the person to edit: ")
                    pos = address_book_main.findByName(name, current_ab)
                    if pos is not None:
                        address_book_main.edit_person(pos, current_ab)
                    else:
                        print("No contacts found")

                # case 4 deletes a contact from the specified address book. If person doesnot exist gives error message
                case 4:
                    name = input("Enter the name of the person to delete: ")
                    pos = address_book_main.findByName(name, current_ab)
                    if pos is not None:
                        del address_book_main.address_book[current_ab][pos]
                        print(f"Contact {name} deleted successfully.")
                    else:
                        print("No contacts found")

                # case 5 adds multiple contacts to specified address book
                case 5:
                    n = int(input("Enter number of persons to add: "))
                    for _ in range(n):
                        address_book_main.get_info(current_ab)

                # case 6 adds multiple address books
                case 6:
                    address_book_main.add_multiple_address_books()

                # case 7 switches between address books
                case 7:
                    print("Available address books:", list(address_book_main.address_book.keys()))
                    new_ab = input("Enter the name of the address book to switch to: ")
                    if new_ab in address_book_main.address_book:
                        current_ab = new_ab
                        print(f"Switched to address book: {new_ab}")
                    else:
                        print("Address book not found.")

                case 8:
                    print("Press 1 to search by city and 2 to search by state")
                    ch = input("Enter your choice: ")
                    if ch == '1':
                        address_book_main.search_person_by_city()
                    elif ch == '2':
                        address_book_main.search_by_state()
                    else:
                        print("Invalid choice")

                case 9:
                    print("Press 1 to get count by city and 2 to get count by state")
                    ch = input("Enter your choice: ")
                    if ch == '1':
                        address_book_main.get_count_by_city()
                    elif ch == '2':
                        address_book_main.get_count_by_state()
                    else:
                        print("Invalid choice")

                case 10:
                    print()
                    print("Sort By name")
                    address_book_main.sort_by_name(current_ab)

                case 11:
                    print("Exiting Main")
                    break
                    

if __name__ == "__main__":

    Main.start()