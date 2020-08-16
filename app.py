from flask import Flask, render_template, redirect, url_for
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
        return redirect(url_for("/"))
