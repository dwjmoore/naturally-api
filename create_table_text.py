import sqlite3

def create_text_db():
    con = sqlite3.connect('database.db')
    print("Opened database successfully")
    cur = con.cursor()

    cur.execute("DROP TABLE textbook")

    cur.execute("""
        CREATE TABLE textbook (
            language    TEXT NOT NULL,
            chapter INTEGER NOT NULL,
            title   TEXT    NOT NULL,
            text    TEXT    NOT NULL
        );
    """)

    print("Created table.")
    con.close()

def insert_text(text):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("INSERT INTO textbook (language,chapter,title,text) VALUES (?,?,?,?)",
        (text["language"],
        text["chapter"],
        text["title"],
        text["text"])
    )

    con.commit()
    print("Text added")
    con.close


create_text_db()

f1 = open("./french/textbook/chapter_1.txt")
fr_text_1 = f1.read()
f1.close()

f2 = open("./french/textbook/chapter_2.txt")
fr_text_2 = f2.read()
f2.close()

f2 = open("./french/textbook/chapter_2.txt")
fr_text_2 = f2.read()
f2.close()

f3 = open("./french/textbook/chapter_3.txt")
fr_text_3 = f3.read()
f3.close()

f4 = open("./french/textbook/chapter_4.txt")
fr_text_4 = f4.read()
f4.close()

f5 = open("./french/textbook/chapter_5.txt")
fr_text_5 = f5.read()
f5.close()

fr_chapter_1 = {
    "language" : "french",
    "chapter" : 1,
    "title" : "Les Duclos",
    "text" : fr_text_1
}

fr_chapter_2 = {
    "language" : "french",
    "chapter" : 2,
    "title" : "La Famille",
    "text" : fr_text_2
}

fr_chapter_3 = {
    "language" : "french",
    "chapter" : 3,
    "title" : "L’Année",
    "text" : fr_text_3
}

fr_chapter_4 = {
    "language" : "french",
    "chapter" : 4,
    "title" : "Les Grand-parents",
    "text" : fr_text_4
}

fr_chapter_5 = {
    "language" : "french",
    "chapter" : 5,
    "title" : "Villes et Pays",
    "text" : fr_text_5
}

insert_text(fr_chapter_1)
insert_text(fr_chapter_2)
insert_text(fr_chapter_3)
insert_text(fr_chapter_4)
insert_text(fr_chapter_5)


i1 = open("./italian/textbook/chapter_1.txt")
i_text_1 = i1.read()
i1.close()

i2 = open("./italian/textbook/chapter_2.txt")
i_text_2 = i2.read()
i2.close()

i2 = open("./italian/textbook/chapter_2.txt")
i_text_2 = i2.read()
i2.close()

i3 = open("./italian/textbook/chapter_3.txt")
i_text_3 = i3.read()
i3.close()

i4 = open("./italian/textbook/chapter_4.txt")
i_text_4 = i4.read()
i4.close()

i5 = open("./italian/textbook/chapter_5.txt")
i_text_5 = i5.read()
i5.close()

i_chapter_1 = {
    "language" : "italian",
    "chapter" : 1,
    "title" : "La Famiglia Rossi",
    "text" : i_text_1
}

i_chapter_2 = {
    "language" : "italian",
    "chapter" : 2,
    "title" : "Città e Paesi",
    "text" : i_text_2
}

i_chapter_3 = {
    "language" : "italian",
    "chapter" : 3,
    "title" : "Nomi e Cognomi",
    "text" : i_text_3
}

i_chapter_4 = {
    "language" : "italian",
    "chapter" : 4,
    "title" : "L'Anno",
    "text" : i_text_4
}

i_chapter_5 = {
    "language" : "italian",
    "chapter" : 5,
    "title" : "Le Stagioni",
    "text" : i_text_5
}

insert_text(i_chapter_1)
insert_text(i_chapter_2)
insert_text(i_chapter_3)
insert_text(i_chapter_4)
insert_text(i_chapter_5)