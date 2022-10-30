import sqlite3

def get_blog_posts():
    blog_posts = []
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM blog ORDER BY blog_post_id DESC")
    rows = cur.fetchall()

    blog_posts = []

    for i in rows:
        blog_post = {}
        blog_post["blog_post_id"] = i["blog_post_id"]
        blog_post["date"] = i["date"]
        blog_post["title"] = i["title"]
        blog_post["body"] = i["body"]
        
        blog_posts.append(blog_post)
    
    return blog_posts