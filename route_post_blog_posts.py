import sqlite3
from flask import jsonify, session
from datetime import datetime

def post_blog_posts(blog_post):
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"error": "Unauthorized"}), 401
    if user_type != 1980:
        return jsonify({"error": "Unauthorized"}), 401

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    date = datetime.now().strftime("%m-%d-%Y")

    cur.execute("INSERT INTO blog (date,title,body) VALUES (?,?,?)",
        (date,
        blog_post['title'],
        blog_post['body'])
    )

    con.commit()
    con.close

    return jsonify({"msg": "Success"}), 201