import sqlite3
def create_questions(path_to_db):
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    image_path TEXT, 
    answer_1 TEXT NOT NULL, 
    answer_2 TEXT NOT NULL, 
    answer_3 TEXT NOT NULL, 
    answer_4 TEXT NOT NULL
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

    questions = [
        ("Що означає цей дорожній знак?", "1.png", ),
        ("Що означає цей дорожній знак?", "2.png"),
        ("Що означає цей дорожній знак?", "3.png"),
        ("Що означає цей дорожній знак?", "4.png"),
        ("Що означає цей дорожній знак?", "5.png")
    ]

    cursor.executemany("INSERT INTO questions (question_text, image_path, answer_1, answer_2, answer_3, answer_4) VALUES (?, ?, ?, ?, ?, ?)", questions)

    conn.commit()
    conn.close()


def add_answers(path_to_db):
    conn = sqlite3.connect(path_to_db)
    cursor = conn.cursor()

    
    cursor.execute("SELECT id FROM questions")
    questions = cursor.fetchall()

    
    for question in questions:
        question_id = question[0]
        print(f"Відповіді для питання #{question_id}:")
        
        correct_answer = input("Введіть правильну відповідь: ")
        wrong_1 = input("Введіть першу неправильну відповідь: ")
        wrong_2 = input("Введіть другу неправильну відповідь: ")
        wrong_3 = input("Введіть третю неправильну відповідь: ")

        
        cursor.execute("INSERT INTO answers (question_id, answer_text, is_correct) VALUES (?, ?, ?)",
                       (question_id, correct_answer, 1))

        
        cursor.execute("INSERT INTO answers (question_id, answer_text, is_correct) VALUES (?, ?, ?)",
                       (question_id, wrong_1, 0))
        cursor.execute("INSERT INTO answers (question_id, answer_text, is_correct) VALUES (?, ?, ?)",
                       (question_id, wrong_2, 0))
        cursor.execute("INSERT INTO answers (question_id, answer_text, is_correct) VALUES (?, ?, ?)",
                       (question_id, wrong_3, 0))

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

def print_all_answers():
    conn = sqlite3.connect("site.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT question_text FROM questions")
    answers = cursor.fetchall()
    
    for answer in answers:
        print(answer)
    conn.close()
    return answers
    
def print_all_questions():
    conn = sqlite3.connect("site.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT answer_text FROM questions")
    answers = cursor.fetchall()
    
    for answer in answers:
        print(answer)
    conn.close()
    return answers




create_questions("site.db")
# create_answers("site.db")
# insert_to_question("site.db")
# print_all_answers()
print('1')
# add_answers("site.db")