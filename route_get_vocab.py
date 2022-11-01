import sqlite3

def get_vocab(language, chapter):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM vocab WHERE language = ? AND chapter = ?",
    [language,
    chapter]
    )
    rows = cur.fetchall()

    vocab = []

    for i in rows:
        word = {}
        word["vocab_id"] = i["vocab_id"]
        word["word"] = i["word"]

        vocab.append(word)
    
    return vocab