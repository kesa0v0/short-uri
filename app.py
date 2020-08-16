from flask import Flask, render_template
from server import get_request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def redirection():
    return get_request()