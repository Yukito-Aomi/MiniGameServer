# -*- coding: utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)


# URL: http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
