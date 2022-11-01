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

    #extracting base64 data from file sent by the front end
    image_data = post['image']
    image_dataURL = str(image_data['dataURL'])

    date = datetime.now().strftime("%m-%d-%Y")

    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("INSERT INTO blog (date, title, body, image, image_url) VALUES (?,?,?,?,?)",
        (date,
        post['title'],
        post['body'],
        image_dataURL,
        post['image_url'])
    )

    con.commit()
    con.close

    con_2 = sqlite3.connect('database.db')
    con_2.row_factory = sqlite3.Row
    cur_2 = con_2.cursor()
    cur_2.execute("SELECT * FROM blog ORDER BY blog_post_id DESC LIMIT 1")
    row = cur_2.fetchone()

    blog_post = {}
    blog_post["blog_post_id"] = row["blog_post_id"]
    blog_post["date"] = row["date"]
    blog_post["title"] = row["title"]
    blog_post["body"] = row["body"]
    blog_post["image"] = row["image"]
    blog_post["image_url"] = row["image_url"]

    return jsonify(blog_post)