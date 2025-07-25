class Contact:
    def __init__(self, name, phone, email, address, place, note):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.place = place
        self.note = note

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "place": self.place,
            "note": self.note
        }
