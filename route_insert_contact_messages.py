import sqlite3
from datetime import datetime

def insert_messages(message):
    date = datetime.now().strftime("%Y-%m-%d, %H:%M")

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO contact_messages (datetime,name,email,subject,message) VALUES (?,?,?,?,?)",
        (date,
        message['name'],
        message['email'],
        message['subject'],
        message['message'])
    )
    con.commit()
    con.close

    return "Success!"