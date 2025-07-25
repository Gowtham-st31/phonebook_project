from controllers.controller import PhoneBookController

def main():
    controller = PhoneBookController()
    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        match choice:
            case "1": controller.add_contact()
            case "2": controller.view_contacts()
            case "3": controller.search_contact()
            case "4": controller.update_contact()
            case "5": controller.delete_contact()
            case "6": break
            case _: print("Invalid option.")

if __name__ == "__main__":
    main()