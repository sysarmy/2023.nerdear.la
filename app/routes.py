from app import app
from flask import render_template


@app.route("/")
def index():
    user = {"username": "Miguel"}
    return render_template("index.html", title="Home", user=user)
