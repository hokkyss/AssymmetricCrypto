# app.py

import os
from typing import Dict, Union

from utils.MainModule import generateKey, proceed, readFile
from utils.utils import PrimeGenerator
from flask import Flask, render_template, request

DEV = os.getenv("FLASK_ENV", "development")
app = Flask(__name__)

<<<<<<< HEAD
PrimeGenerator.fill()

@app.route("/upload_public_key", methods=["POST"])
=======
@app.route("/upload_public_key", methods=['POST'])
>>>>>>> c90e4d64db86f22de786c528fac84c2bd9961f60
def upload_public_key():
    filename = request.json.get("public-key-file")
    return readFile(filename)

@app.route("/upload_private_key", methods=['POST'])
def upload_private_key():
    filename = request.json.get("private-key-file")
    return readFile(filename)

@app.route("/generation", methods=["GET", 'POST'])
def generation():
    notification = ""
    if (request.method == 'POST'):
        choice = request.json.get("choice")
        notification = generateKey(choice)
        return notification
    else:
        return render_template("generation.html")

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

<<<<<<< HEAD
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
=======
@app.route("/execute", methods=['POST'])
def execute():
    public_key = request.json.get("public-key")
    private_key = request.json.get("private-key")
    choice = request.json.get("choice")
    mode = request.json.get("mode")
    input_box = request.json.get("input-box")
    result_box = proceed(public_key, private_key, choice, mode, input_box)
    return result_box
>>>>>>> c90e4d64db86f22de786c528fac84c2bd9961f60

@app.route("/guideline", methods=['GET'])
def guideline():
    return render_template("guideline.html")

if __name__ == '__main__':
    app.run(debug=DEV)