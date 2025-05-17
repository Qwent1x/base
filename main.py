import sqlite3
import sql


from flask import Flask
from flask import render_template
actual_answer = 0

app = Flask(__name__, template_folder = 'html')

@app.route("/starts_questions")
def start():
    global actual_answer
    answers = sql.print_all_answers()
    question = "Що значить цей знак?"
    a = answers[actual_answer]
    b = answers[actual_answer+1]
    c = answers[actual_answer+2]
    d = answers[actual_answer+3]
    img = "photos/1.png"
    if actual_answer <= 20:
        actual_answer += 4
        return render_template("index2.html",question=question,a=a,b=b,c=c,d=d,img=img)
    else: 
        return render_template('index3.html')

    
@app.route("/")
def start1():
    return render_template("index.html")
@app.route('/finish')
def finish():
    return render_template('index3.html')
    
correct = [("")]
uncorrect = [("")]



app.run()