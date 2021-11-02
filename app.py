# app.py

import os
from typing import Dict, Union

from utils.main import generateKey, proceed
from utils.utils import PrimeGenerator
from flask import Flask, render_template, request

DEV = os.getenv("FLASK_ENV", "development")
app = Flask(__name__)

PrimeGenerator.fill()

@app.route("/upload_public_key", methods=["POST"])
def upload_public_key():
    if (request.method == "POST"):
        filename = request.json.get("public-key-file")
        print(filename)
        f = open("keys/" + filename, "r")
        output_text = f.read()
        return output_text
    else:
        return ""

@app.route("/upload_private_key", methods=["POST"])
def upload_private_key():
    if request.method == "POST":
        filename = request.json.get("private-key-file")
        print(filename)
        f = open("keys/" + filename, "r")
        output_text = f.read()
        return output_text
    else:
        return ""

@app.route("/generation", methods=["GET", "POST"])
def generation():
    output_text = ""
    if (request.method == "POST"):
        choice = request.json.get("choice")
        all_keys, full_path = generateKey(choice)
        output_text = "Generate key success! Saved on " + full_path
        return output_text
    else:
        return render_template("generation.html")

@app.route("/", methods=['GET'])
def encryption():
    return render_template("home.html")

@app.route("/count", methods=["POST"])
def count():
    result: Dict[str, str] = { "result": "", "error": None }
    try:
        public_key = request.json.get("public-key")
        private_key = request.json.get("private-key")
        choice = request.json.get("choice")
        mode = request.json.get("mode")
        input_box = request.json.get("input-box")
        result_box = proceed(public_key, private_key, choice, mode, input_box)

        if not result_box: result_box = ""
        result["result"] = result_box
    except ValueError as e:
        result["error"] = str(e)

    return result

if __name__ == '__main__':
    app.run(debug=DEV)
