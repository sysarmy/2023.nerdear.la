from app import app
from flask import render_template


@app.route("/")
def index():
    user = {"username": "this is a test :) "}
    accordion_dataset = [
        {
            "number": 1,
            "title": "Que es Nerdearla",
            "description": "Nerdearla es lorem ipsum bla bla bla",
        },
        {
            "number": 2,
            "title": "Cuando se hace la Nerdearla",
            "description": "La respuesta esta en tu corazon",
        },
        {
            "number": 3,
            "title": "Cúanto sale?",
            "description": "Paga Jolo",
        },
    ]
    return render_template(
        "base.html", title="Home", accordion_dataset=accordion_dataset
    )
