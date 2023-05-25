from app import app
from app.forms import ContactForm
from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    jsonify,
    abort,
    make_response,
)


# TODO: Please for the love of god change the secret key generation
import os

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/", methods=["POST", "GET"])
def index():
    # The data to put in the faq accordion
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
    contact_form = ContactForm()
    return render_template(
        "index.html",
        title="Home",
        accordion_dataset=accordion_dataset,
        form=contact_form,
    )


@app.route("/sponsors")
def sponsors():
    return render_template("sponsors.html", title="Sponsors")


@app.route("/code_of_conduct")
def code_of_conduct():
    return render_template("code_of_conduct.html", title="Code of Conduct")


@app.route("/submit_contact", methods=["POST"])
def contact():
    # Parse the incoming request body (a JSON Object) and convert it to a dictionary
    print("Got a submit contact request")
    req = request.get_json()
    print(req)

    res = make_response(
        jsonify(
            {
                "message": "JSON recieved successfully",
                "name": req["name"],
                "surname": req["surname"],
            }
        ),
        200,
    )

    return res
