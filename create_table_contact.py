import sqlite3

def create_contact_db():
    con = sqlite3.connect('database.db')
    print("Opened database successfully")
    cur = con.cursor()

    cur.execute("DROP TABLE contact_messages")

    cur.execute("""
        CREATE TABLE contact_messages (
            message_id  INTEGER PRIMARY KEY NOT NULL,
            datetime    TEXT    NOT NULL,
            name    TEXT    NOT NULL,
            email   TEXT    NOT NULL,
            subject TEXT    NOT NULL,
            message TEXT    NOT NULL
        );
    """)

    print("Created table.")
    con.close()

create_contact_db()