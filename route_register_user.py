import sqlite3
from flask import jsonify
import bcrypt

def register_user(user):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT email FROM users WHERE email = ?", [user['email']])
    email = res.fetchone()

    if email is None:
        password = user['password'].encode('UTF-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        cur.execute("INSERT INTO users (email,password,user_type,language) VALUES (?,?,?,?)",
            (user['email'],
            hashed,
            2018,
            "NO_LANGUAGE")
        )
        con.commit()
        con.close

        return jsonify({"msg": "Success"}), 201

    elif user['email'] == email[0]:
        return jsonify({"msg": "Email alreay registered"}), 409