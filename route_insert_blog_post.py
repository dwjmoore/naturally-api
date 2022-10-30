import sqlite3
from datetime import datetime
from flask import session, jsonify

def insert_blog_post(post):
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"error": "Unauthorized"}), 401
    if user_type != 1980:
        return jsonify({"error": "Unauthorized"}), 401

    date = datetime.now().strftime("%Y-%m-%d, %H:%M")

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("INSERT INTO blog (date, title, body, image) VALUES (?,?,?,?)",
        (date,
        post['title'],
        post['body'],
        post['image'])
    )

    con.commit()
    con.close

    return jsonify({"msg" : "Success!"})