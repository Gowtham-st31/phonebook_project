class PhoneBookView:
    def get_contact_input(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        place = input("Enter place: ")
        note = input("Enter note: ")
        return name, phone, email, address, place, note

    def display_contacts(self, contacts):
        for c in contacts:
            print(f"Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}, Address: {c[3]}, Place: {c[4]}, Note: {c[5]}")

    def display_message(self, message):
        print(message)

    def get_search_key(self):
        return input("Search by name, phone, place, or note: ")

    def get_name_to_delete(self):
        return input("Enter name to delete: ")

    def get_name_to_update(self):
        return input("Enter name to update: ")

    def get_updated_contact_input(self, old_data):
        email = input(f"New email ({old_data[2]}): ") or old_data[2]
        phone = input(f"New phone ({old_data[1]}): ") or old_data[1]
        address = input(f"New address ({old_data[3]}): ") or old_data[3]
        place = input(f"New place ({old_data[4]}): ") or old_data[4]
        note = input(f"New note ({old_data[5]}): ") or old_data[5]
        return old_data[0], phone, email, address, place, note
