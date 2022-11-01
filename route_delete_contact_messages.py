import sqlite3
from flask import jsonify, session

def delete_messages(id):
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"error": "Unauthorized"}), 401
    if user_type != 1980:
        return jsonify({"error": "Unauthorized"}), 401

    id = int(id)

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("DELETE FROM contact_messages WHERE message_id = ?", [id])
    con.commit()
    cur.close()

    return jsonify({"msg" : "Success!" })