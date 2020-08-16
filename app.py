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
    print("="*10+"INCOMING REDIRECTION REQUEST"+"="*10)
    print("receiving:", link)
    data = db.select(link)[0][1]
    print("redirect to:", data)
    if data:
        return redirect(data)
    else:
        return redirect(url_for("index"))


@app.route('/convert', methods=['POST'])
def convert():
    print("="*10+"INCOMING CONVERT REQUEST"+"="*10)
    value = request.form['link']
    print("received link:", value)
    shorturl = "http://shorturl.kesa0v0.codes/link/" + generator.generate(value, db)
    print("shortened link:", shorturl)
    return shorturl
