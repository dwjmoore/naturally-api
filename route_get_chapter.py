import sqlite3

def get_chapter(lang_chap):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM textbook WHERE language = ? AND chapter = ?",
    [lang_chap['language'],
    lang_chap['chapter']]
    )
    row = cur.fetchone()

    text = {}
    text["language"] = row["language"]
    text["chapter"] = row["chapter"]
    text["title"] = row["title"]
    text["text"] = row["text"]
    
    return text