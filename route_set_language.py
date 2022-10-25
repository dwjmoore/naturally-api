import sqlite3
from flask import jsonify, session

def set_language(language):
    email = session.get("email")

    if not email:
        return jsonify({"error": "Unauthorized"}), 401

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("Update users SET language = ? WHERE email = ?",
        (language["language"],
        email)
    )

    con.commit()
    con.close
    
    return jsonify({"msg" : f"Success! Langauge has been set to {language}."}), 200