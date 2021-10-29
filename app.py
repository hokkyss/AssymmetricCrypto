# app.py

import os
from utils.utils import PrimeGenerator
from flask import Flask, render_template

DEV = os.getenv("FLASK_ENV", "development")
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=DEV)
