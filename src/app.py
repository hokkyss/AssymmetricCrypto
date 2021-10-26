# app.py

from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)