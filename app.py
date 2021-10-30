# app.py

import os

from utils.main import proceed
from utils.utils import PrimeGenerator
from flask import Flask, render_template, request

DEV = os.getenv("FLASK_ENV", "development")
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def encryption():
    if request.method == "POST":
        public_key = request.form.get("public-key")
        private_key = request.form.get("private-key")
        choice = todo = request.form.get("choice")
        mode = request.form.get("mode")
        input_box = request.form.get("input-box")
        result_box = proceed(public_key, private_key, choice, mode, input_box)
    else:
        result_box = ""
    print("Result box", result_box)
    return render_template("home.html", result_box = result_box)


if __name__ == '__main__':
    app.run(debug=DEV)
