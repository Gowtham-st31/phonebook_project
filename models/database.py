from .db_connection import get_db_connection

class ContactDB:
    def __init__(self):
        self.conn = get_db_connection()
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            place TEXT,
            note TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_contact(self, contact):
        query = '''
        INSERT INTO contacts (name, phone, email, address, place, note)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, (
            contact["name"],
            contact["phone"],
            contact["email"],
            contact["address"],
            contact["place"],
            contact["note"]
        ))
        self.conn.commit()

    def search_contacts(self, keyword):
        query = '''
        SELECT * FROM contacts
        WHERE name LIKE ? OR phone LIKE ? OR place LIKE ? OR note LIKE ?
        '''
        like_keyword = f"%{keyword}%"
        cursor = self.conn.execute(query, (like_keyword, like_keyword, like_keyword, like_keyword))
        return cursor.fetchall()

    def get_all_contacts(self):
        cursor = self.conn.execute("SELECT * FROM contacts")
        return cursor.fetchall()
