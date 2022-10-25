import sqlite3
from flask import jsonify, session

def get_messages():
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"error": "Unauthorized"}), 401
    if user_type != 1980:
        return jsonify({"error": "Unauthorized"}), 401

    messages = []
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM contact_messages")
    rows = cur.fetchall()

    for i in rows:
        message = {}
        message["message_id"] = i["message_id"]
        message["datetime"] = i["datetime"]
        message["name"] = i["name"]
        message["email"] = i["email"]
        message["subject"] = i["subject"]
        message["message"] = i["message"]
        messages.append(message)
    
    return messages