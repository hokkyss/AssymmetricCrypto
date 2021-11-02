# app.py

import os
import random
from typing import Dict, Union

from utils.EllipticCurve import EllipticCurve
from utils.MainModule import generateKey, proceed, readFile
from utils.utils import PrimeGenerator
from flask import Flask, render_template, request, url_for

DEV = os.getenv("FLASK_ENV", "development") == "development"
app = Flask(__name__)

PrimeGenerator.fill()
EllipticCurve.generate()

@app.route("/generation", methods=["GET", 'POST'])
def generation():
    if (request.method == 'POST'):
        notification = { "result": "", "public": "", "private": "", "DEV": DEV, "error": "" }
        try:
            choice = request.json.get("choice")
            [public_key, private_key, filename] = generateKey(choice)

            full_path = "static/" + filename

            f = open(full_path + ".pub", 'w')
            f.write(public_key)
            f.close()

            f = open(full_path + ".pri", 'w')
            f.write(private_key)
            f.close()

            notification["result"] = f"\nGenerate key success! Saved as {filename}.pub and {filename}.pri"
            notification["result"] += "\nPublic key : " + public_key
            notification["result"] += "\nPrivate key : " + private_key

            notification["private"] = url_for('static', filename=f'{filename}.pri')
            notification["public"] = url_for('static', filename=f'{filename}.pub')
            notification["filename"] = filename
        except ValueError as e:
            notification["error"] = str(e)

        return notification
    else:
        return render_template("generation.html")

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/execute", methods=["POST"])
def execute():
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

@app.route("/get-content", methods=["POST"])
def file_content():
    file = request.files.get('file')
    return file.stream.read().decode()

@app.route("/guideline", methods=['GET'])
def guideline():
    return render_template("guideline.html")

if __name__ == '__main__':
    app.run(debug=DEV)