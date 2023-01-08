import sqlite3

def create_questions_db():
    con = sqlite3.connect('database.db')
    print("Opened database successfully")
    cur = con.cursor()

    # cur.execute("DROP TABLE fill_in_blank")

    cur.execute("""
        CREATE TABLE questions (
            question_id INTEGER PRIMARY KEY NOT NULL,
            language    TEXT    NOT NULL,
            chapter INTEGER NOT NULL,
            question  TEXT    NOT NULL,
            answer  TEXT    NOT NULL
        );
    """)

    print("Created table.")
    con.close()

def insert_questions(questions, answers):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    language = 'french'
    chapter = 1

    for i in range(len(questions)):
        cur.execute("INSERT INTO fill_in_blank (language,chapter,question,answer) VALUES (?,?,?,?)",
            (language,
            chapter,
            questions[i],
            answers[i])
        )

    con.commit()
    print("Text added")
    con.close


create_questions_db()

questions = []
answers = []

#Update the file names for future entries from other chapters.
with open("./french/questions/chapter_1_questions.txt") as f:
    for line in f:
        questions.append(line.strip())
f.close()

with open("./french/questions/chapter_1_answers.txt") as f:
    for line in f:
        answers.append(line.strip())
f.close()

insert_questions(questions, answers)