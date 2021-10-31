# app.py

import os
from typing import Dict, Union

from utils.main import proceed
from utils.utils import PrimeGenerator
from flask import Flask, json, render_template, request

DEV = os.getenv("FLASK_ENV", "development")
app = Flask(__name__)

@app.route("/", methods=['GET'])
def encryption():
    return render_template("home.html")

@app.route("/count", methods=["POST"])
def count():
    result: Dict[str, Union[str, int, None]] = {}
    if request.method == "POST":
        public_key = request.json.get("public-key")
        private_key = request.json.get("private-key")
        choice = request.json.get("choice")
        mode = request.json.get("mode")
        input_box = request.json.get("input-box")
        result_box = proceed(public_key, private_key, choice, mode, input_box)
    else:
        result_box = ""

    if not result_box: result_box = ""

    return result_box

if __name__ == '__main__':
    app.run(debug=DEV)
