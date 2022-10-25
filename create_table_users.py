import sqlite3
import bcrypt

def create_user_db():
    con = sqlite3.connect('database.db')
    print("Opened database successfully")
    cur = con.cursor()

    cur.execute("DROP TABLE users")

    cur.execute("""
        CREATE TABLE users (
            user_id    INTEGER PRIMARY KEY NOT NULL,
            email   TEXT    NOT NULL,
            password    TEXT    NOT NULL,
            user_type   INTEGER NOT NULL,
            language    TEXT    NOT NULL,
            UNIQUE (email)
        );
    """)

    print("Created table.")
    con.close()

def insert_user(user):
    con = sqlite3.connect('database.db')
    cur = con.cursor()


    password = user['password'].encode('UTF-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    cur.execute("INSERT INTO users (email,password,user_type,language) VALUES (?,?,?,?)",
        (user['email'],
        hashed,
        user['user_type'],
        user['language'])
    )

    con.commit()
    print("User added")
    con.close


user_1 = {
    "email" : "dwjmoore@gmail.com",
    "password" : "D@uidi2K00L",
    "user_type" : 1980,
    "language" : "NO_LANGUAGE"
}

user_2 = {
    "email" : "user_2@test.com",
    "password" : "123456789",
    "user_type" : 2018,
    "language" : "NO_LANGUAGE"
}

user_3 = {
    "email" : "user_3@test.com",
    "password" : "123456789",
    "user_type" : 2018,
    "language" : "NO_LANGUAGE"
}

user_4 = {
    "email" : "user_4@test.com",
    "password" : "123456789",
    "user_type" : 2018,
    "language" : "NO_LANGUAGE"
}

user_5 = {
    "email" : "user_5@test.com",
    "password" : "123456789",
    "user_type" : 2018,
    "language" : "NO_LANGUAGE"
}

create_user_db()
insert_user(user_1)
insert_user(user_2)
insert_user(user_3)
insert_user(user_4)
insert_user(user_5)

print("Tasks complete")