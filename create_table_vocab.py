import sqlite3

def create_vocab_db():
    con = sqlite3.connect('database.db')
    print("Opened database successfully")
    cur = con.cursor()

    cur.execute("DROP TABLE vocab")

    cur.execute("""
        CREATE TABLE vocab (
            language    TEXT NOT NULL,
            chapter INTEGER NOT NULL,
            word    TEXT    NOT NULL
        );
    """)

    print("Created table.")
    con.close()

def insert_vocab(words, language, chapter):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    for i in range(len(words)):

        cur.execute("INSERT INTO vocab (language,chapter,word) VALUES (?,?,?)",
            (language,
            chapter,
            words[i])
        )

    con.commit()
    print("Word added")
    con.close


create_vocab_db()

f1_words = []

with open("./french/vocab/chapter_1.txt") as f:
    for line in f:
        f1_words.append(line.strip())
f.close()

insert_vocab(f1_words, 'french', 1)


i1_words = []

with open("./italian/vocab/chapter_1.txt") as f:
    for line in f:
        i1_words.append(line.strip())
f.close()

insert_vocab(i1_words, 'italian', 1)