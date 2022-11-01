import sqlite3

def create_fill_in_blank_db():
    con = sqlite3.connect('database.db')
    print("Opened database successfully")
    cur = con.cursor()

    cur.execute("DROP TABLE fill_in_blank")

    cur.execute("""
        CREATE TABLE fill_in_blank (
            sentence_id INTEGER PRIMARY KEY NOT NULL,
            language    TEXT    NOT NULL,
            chapter INTEGER NOT NULL,
            sentence_front  TEXT    NOT NULL,
            sentence_back    TEXT    NOT NULL,
            answer  TEXT    NOT NULL
        );
    """)

    print("Created table.")
    con.close()

def insert_fill_in_blank(sentences_front, sentences_back, answers):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    language = 'french'
    chapter = 1

    for i in range(len(sentences_front)):

        cur.execute("INSERT INTO fill_in_blank (language,chapter,sentence_front,sentence_back,answer) VALUES (?,?,?,?,?)",
            (language,
            chapter,
            sentences_front[i],
            sentences_back[i],
            answers[i])
        )

    con.commit()
    print("Text added")
    con.close


create_fill_in_blank_db()

sentences_front = []
sentences_back = []
answers = []

#Update the file names for future entries from other chapters.
with open("./french/exercises/fill-in-the-blank/chapter_1_sentences_front.txt") as f:
    for line in f:
        sentences_front.append(line.strip())
f.close()

with open("./french/exercises/fill-in-the-blank/chapter_1_sentences_back.txt") as f:
    for line in f:
        sentences_back.append(line.strip())
f.close()

with open("./french/exercises/fill-in-the-blank/chapter_1_answers.txt") as f:
    for line in f:
        answers.append(line.strip())
f.close()

insert_fill_in_blank(sentences_front, sentences_back, answers)