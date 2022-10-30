import sqlite3
from flask import jsonify, session

def edit_blog_posts(blog_post):
    email = session.get("email")
    user_type = session.get("user_type")
    
    if not email:
        return jsonify({"error": "Unauthorized"}), 401
    if user_type != 1980:
        return jsonify({"error": "Unauthorized"}), 401

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("Update blog SET title = ?, body = ?, image = ? WHERE blog_post_id = ?",
        (blog_post['title'],
        blog_post['body'],
        blog_post['image'],
        blog_post['blog_post_id'])
    )

    con.commit()
    con.close

    return blog_post