import sqlite3

def create_table():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY AUTOINCREMENT, level TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, wrong1 TEXT, wrong2 TEXT, wrong3 TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS quiz_content (id INTEGER PRIMARY KEY AUTOINCREMENT, question_id INTEGER, quiz_id INTEGER, FOREIGN KEY (quiz_id) REFERENCES quiz (id), FOREIGN KEY (question_id) REFERENCES questions (id))")
    conn.commit()
    conn.close()

def add_question():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    question = input("Введіть питання: ")
    answer = input("Введіть правильну відповідь: ")
    wrong_1 = input("Введіть першу неправильну відповідь: ")
    wrong_2 = input("Введіть другу неправильну відповідь: ")
    wrong_3 = input("Введіть третю неправильну відповідь: ")
    cur.execute("INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)", (question, answer, wrong_1, wrong_2, wrong_3))
    conn.commit()
    conn.close()

def add_quiz():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    name = input("Введіть назву вікторини: ")
    cur.execute("INSERT INTO quiz (level) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def link_question_to_quiz():
    conn = sqlite3.connect("quiz.db")
    cur = conn.cursor()
    choice = input("Зв'язати питання з вікториною? (так/ні): ")
    while choice == "так":
        question_id = input("Введіть ID питання: ")
        quiz_id = input("Введіть ID вікторини: ")
        cur.execute("INSERT INTO quiz_content (question_id, quiz_id) VALUES (?, ?)", (question_id, quiz_id))
        conn.commit()
        choice = input("Зв'язати ще одне питання? (так/ні): ")
    conn.close()

create_table()
while input("Додати питання? (так/ні): ") == "так":
    add_question()
while input("Додати вікторину? (так/ні): ") == "так":
    add_quiz()
link_question_to_quiz()