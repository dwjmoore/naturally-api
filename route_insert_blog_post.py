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

    return jsonify({"msg" : "Success!", })