import sqlite3

def create_questions(path_to_db):
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    image_path TEXT
    )
    ''')

    conn.commit()
    conn.close()

def create_answers(path_to_db):
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER,
    answer_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL CHECK (is_correct IN (0, 1)),
    FOREIGN KEY (question_id) REFERENCES questions(id)
    )
    ''')
    conn.commit()
    conn.close()


def insert_to_question(path_to_db):
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO questions (question_text, image_path) VALUES (?, ?)",
               ([["Що означає цей дорожній знак?", "1.png"], ["Що означає цей дорожній знак?", "2.png"],
               ["Що означає цей дорожній знак?", "3.png"], ["Що означає цей дорожній знак?", "4.png"], 
               ["Що означає цей дорожній знак?", "5.png"]]))

    conn.commit()
    conn.close()


def add_answers():
    conn = sqlite3.connect("site.db")
    cur = conn.cursor()
    correct = input("Введіть правильну відповідь: ")
    wrong_1 = input("Введіть першу неправильну відповідь: ")
    wrong_2 = input("Введіть другу неправильну відповідь: ")
    wrong_3 = input("Введіть третю неправильну відповідь: ")
    cur.execute("INSERT INTO answers (correct, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?)", (correct, wrong_1, wrong_2, wrong_3))
    conn.commit()
    conn.close()


# def select(sql, param = None):
#     conn=sqlite3.Connection("site.db")
#     cur =conn.cursor()
#     if param:
#         cur.execute(sql, param)
#     else:
#         cur.execute(sql)
#     data = cur.fetchall()
#     conn.close()
#     return data
