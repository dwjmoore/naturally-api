import sqlite3
import random

def get_fill_in_blank(language, chapter):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM fill_in_blank WHERE language = ? AND chapter = ?",
        [language,
        chapter]
    )
    rows = cur.fetchall()

    sentences = []

    for i in rows:
        sentence = {}
        sentence["sentence_id"] = i["sentence_id"]
        sentence["language"] = i["language"]
        sentence["chapter"] = i["chapter"]
        sentence["sentence_front"] = i["sentence_front"]
        sentence["sentence_back"] = i["sentence_back"]
        sentence["answer"] = i["answer"]
        sentences.append(sentence)
    
    return sentences

def get_random_sentence(language, chapter):
    sentences = get_fill_in_blank(language, chapter)
    random_sentence = random.choice(sentences)

    return random_sentence