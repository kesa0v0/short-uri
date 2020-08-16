from flask import Flask, render_template, redirect, url_for, request
import generator
from database import DB

app = Flask(__name__)
db = DB()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/link/<link>')
def redirection(link):
    print("receiving:", link)
    data = db.select(link)
    print("redirect to:", data)
    if data:
        return redirect(data)
    else:
        return redirect(url_for("index"))


@app.route('/convert', methods=['POST'])
def convert():
    value = request.form['link']
    shorturl = generator.generate(value)
    return shorturl
