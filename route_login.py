import sqlite3
from flask import jsonify, session
import bcrypt

def login(user):
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur= con.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", [user['email']])
    row = cur.fetchone()

    if row is None:
        return jsonify({"msg": "Bad email or password"}), 401
    else:
        stored_user = {}
        stored_user["user_id"] = row["user_id"]
        stored_user["email"] = row["email"]
        stored_user["password"] = row["password"]
        stored_user["user_type"] = row["user_type"]

        supplied_password = user['password'].encode('UTF-8')

    if bcrypt.checkpw(supplied_password, stored_user["password"]):
        session["email"] = stored_user["email"]
        session["user_type"] = stored_user["user_type"]
        return jsonify({ "email": stored_user["email"], "role": stored_user["user_type"], "msg": "User is logged in."})
    else:
        return jsonify({"msg": "Bad email or password"}), 401