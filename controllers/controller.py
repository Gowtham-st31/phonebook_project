from models.database import ContactDB
from models.contact import Contact
from views.view import PhoneBookView

class PhoneBookController:
    def __init__(self):
        self.model = ContactDB()
        self.view = PhoneBookView()

    def add_contact(self):
        name, phone, email, address, place, note = self.view.get_contact_input()
        contact = Contact(name, phone, email, address, place, note)
        self.model.add(contact)
        self.view.display_message("Contact added.")

    def view_contacts(self):
        contacts = self.model.get_all()
        self.view.display_contacts(contacts)

    def search_contact(self):
        key = self.view.get_search_key()
        result = self.model.find(key)
        if result:
            self.view.display_contacts([result])
        else:
            self.view.display_message("Not found.")

    def delete_contact(self):
        name = self.view.get_name_to_delete()
        deleted = self.model.delete(name)
        self.view.display_message("Deleted." if deleted > 0 else "No contact found.")

    def update_contact(self):
        name = self.view.get_name_to_update()
        old_data = self.model.get_by_name(name)
        if old_data:
            name, phone, email, address, place, note = self.view.get_updated_contact_input(old_data)
            updated = Contact(name, phone, email, address, place, note)
            self.model.update(name, updated)
            self.view.display_message("Updated.")
        else:
            self.view.display_message("Contact not found.")
