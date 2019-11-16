from app import app
from flask import render_template
from app.forms import AddPost

@app.route("/")
def index():
    guest = {"name": "guest"}
    return render_template("index.html", guest=guest)

@app.route("/add-post")
def add_post():
    form = AddPost()
    return render_template("add_post.html", form=form)
