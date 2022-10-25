import sqlite3
import random

def get_fill_in_blank(lang_chap):
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM fill_in_blank WHERE language = ? AND chapter = ?",
        [lang_chap['language'],
        lang_chap['chapter']]
    )
    rows = cur.fetchall()

    sentences = []

    for i in rows:
        sentence = {}
        sentence["sentence"] = i["sentence"]
        sentence["answer"] = i["answer"]
        sentences.append(sentence)
    
    return sentences

def get_random_sentence(lang_chap):
    sentences = get_fill_in_blank(lang_chap)
    random_sentence = random.choice(sentences)

    return random_sentence