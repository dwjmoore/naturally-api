import sqlite3

def get_vocab(lang_chap):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM vocab WHERE language = ? AND chapter = ?",
    [lang_chap['language'],
    lang_chap['chapter']]
    )
    rows = cur.fetchall()

    vocab = []

    for i in rows:
        word = i["word"]
        vocab.append(word)
    
    return vocab