from app import app
from flask import render_template

@app.route("/")
def index():
    guest = {"name": "guest"}
    return render_template("index.html", guest=guest)

@app.route("/add-post")
def add_post():
    return render_template("add_post.html")