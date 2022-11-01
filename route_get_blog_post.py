import sqlite3

def get_blog_post(blog_post_id):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM blog WHERE blog_post_id = ?", [blog_post_id])
    row = cur.fetchone()

    blog_post = {}
    blog_post["blog_post_id"] = row["blog_post_id"]
    blog_post["date"] = row["date"]
    blog_post["title"] = row["title"]
    blog_post["body"] = row["body"]
    blog_post["image"] = row["image"]
    blog_post["image_url"] = row["image_url"]
    
    return blog_post