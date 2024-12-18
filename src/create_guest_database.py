import sqlite3

def create_guest_database():
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            previous_stays TEXT,
            room_preferences TEXT,
            activities TEXT,
            dining_choices TEXT,
            feedback TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_guest_database()
