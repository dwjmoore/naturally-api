import sqlite3

def get_chapters(language):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM textbook WHERE language = ?", [language])
    rows = cur.fetchall()

    chapters = []

    for i in rows:
        chapter = {}
        chapter["language"] = i["language"]
        chapter["chapter"] = i["chapter"]
        chapter["title"] = i["title"]
        chapter["text"] = i["text"]
        chapter["link"] = i["link"]
        
        chapters.append(chapter)
    
    return chapters