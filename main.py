import sqlite3
import sql


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/starts_questions")
def start():
    answers = sql.print_all_answers()
    question = "Що значить цей знак?"
    a = answers[0]
    b = answers[1]
    c = answers[2]
    d = answers[3]
    img = "photos/1.png"
    return render_template("index2.html",question=question,a=a,b=b,c=c,d=d,img=img)
@app.route("/")
def start1():
    return render_template("index.html")




app.run()