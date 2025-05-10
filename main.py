import sqlite3


from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/starts_questions")
def start():
    return render_template("index2.html")
@app.route("/")
def start1():
    return render_template("index.html")




app.run()