from flask import jsonify, session
import sqlite3

def check_language():
    email = session.get("email")

    if not email:
        return jsonify({"logged_in": False}), 200

    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", [email])
    row = cur.fetchone()

    language = row["language"]
    
    return jsonify({"language": language}), 200