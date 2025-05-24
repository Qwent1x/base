import sqlite3
import sql
import random
from flask import Flask, render_template

actual_answer = 0

app = Flask(__name__)

@app.route("/starts_questions")
def start():
    global actual_answer
    questions = sql.get_all_questions()

    if actual_answer >= len(questions):
        return render_template('index3.html')

    # Витягуємо одне питання
    question_text = questions[actual_answer][0]
    image_path = questions[actual_answer][1]
    answer_1 = questions[actual_answer][2]
    answer_2 = questions[actual_answer][3]
    answer_3 = questions[actual_answer][4]
    answer_4 = questions[actual_answer][5]

    # Список відповідей
    answer_options = [answer_1, answer_2, answer_3, answer_4]
    random.shuffle(answer_options)

    actual_answer += 1

    return render_template(
        "index2.html",
        question=question_text,
        img=image_path,
        a=answer_options[0],
        b=answer_options[1],
        c=answer_options[2],
        d=answer_options[3]
    )

@app.route("/")
def start1():
    return render_template("index.html")

@app.route('/finish')
def finish():
    return render_template('index3.html')

correct = [("")]
uncorrect = [""]

app.run()
