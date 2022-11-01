import sqlite3

def get_chapter(language, chapter):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM textbook WHERE language = ? AND chapter = ?",
    [language,
    chapter]
    )
    row = cur.fetchone()

    text = {}
    text["language"] = row["language"]
    text["chapter"] = row["chapter"]
    text["title"] = row["title"]
    text["text"] = row["text"]
    text["link"] = row["link"]
    
    return text