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
import csv
from app.functions import *

SPONSORS_FILE = "sponsors.csv"
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
    category_order = {
        "bronze": 1,
        "silver": 2,
        "gold": 3,
        "diamond": 4,
        "adamantium": 5,
    }
    # Get a list of dictionaries based on a CSV file
    sponsors = csv_to_list_of_dicts(SPONSORS_FILE)
    # Convert key values to lowercase, just in case the input in the CSV is in caps
    convert_key_values_to_lowercase(sponsors, "category")
    # Sort the sponsors by the category_order dictionary
    # This makes the category with the highest number appear first
    sponsors = sorted(
        sponsors, key=lambda x: category_order[x["category"]], reverse=True
    )
    # Group the sponsors by category.
    # grouped_sponsors ends up looking like this:
    """
{
    "adamantium": [
        {
            "name": "icbc",
            "category": "adamantium",
            "file": "icbc.png",
            "link": "https://www.icbc.com.ar",
        },
        {
            "name": "openqube",
            "category": "adamantium",
            "file": "openqube.png",
            "link": "https://openqube.io/",
        },
        {
            "name": "google cloud platform",
            "category": "adamantium",
            "file": "googlecloud.png",
            "link": "https://cloud.google.com/",
        },
    ],
    "diamond": [
        {
            "name": "cognizant",
            "category": "diamond",
            "file": "cognizant.png",
            "link": "https://sysar.my/cognizantsoftvision",
        },
        {
            "name": "cognizant soft vision",
            "category": "diamond",
            "file": "cognizantsoftvision.png",
            "link": "https://sysar.my/cognizantsoftvision",
        },
        {
            "name": "cognizant soft vision",
            "category": "diamond",
            "file": "cognizantsoftvision.png",
            "link": "https://sysar.my/cognizantsoftvision",
        },
    ],
    "silver": [
        {
            "name": "openqube",
            "category": "silver",
            "file": "openqube.png",
            "link": "https://openqube.io/",
        },
        {
            "name": "openqube",
            "category": "silver",
            "file": "openqube.png",
            "link": "https://openqube.io/",
        },
    ],
}
    """
    grouped_sponsors = {}
    for sponsor in sponsors:
        category = sponsor["category"]
        if category in grouped_sponsors:
            grouped_sponsors[category].append(sponsor)
        else:
            grouped_sponsors[category] = [sponsor]
    return render_template(
        "sponsors.html", title="Sponsors", grouped_sponsors=grouped_sponsors
    )


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
