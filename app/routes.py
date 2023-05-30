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

FAQ_FILE = "datasets/faq.json"
SPONSORS_FILE = "datasets/sponsors.csv"
SPONSORS_CONFIG_FILE = "datasets/sponsors_config.json"
AGENDA_FILE = "datasets/agenda.json"

# TODO: Please for the love of god change the secret key generation
import os

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/", methods=["POST", "GET"])
def index():
    """
    Shows the index page

    Returns:
        flask.Response: The rendered index HTML template.
    """
    # The data to put in the faq accordion
    accordion_dataset = read_json_file(FAQ_FILE)
    contact_form = ContactForm()
    return render_template(
        "index.html",
        title="Home",
        accordion_dataset=accordion_dataset,
        form=contact_form,
    )


@app.route("/sponsors")
def sponsors():
    """
    Renders the sponsors page.

    Reads the sponsors configuration from the specified JSON file and retrieves the list of sponsors from a CSV file.
    The sponsors are sorted and grouped based on the configuration and rendered using the 'sponsors.html' template.

    The csv file should look like this

    ############## sponsors.csv #############

    name,category,file,link
    cognizant,diamond,cognizant.png,https://sysar.my/cognizantsoftvision
    icbc,adamantium,icbc.png,https://www.icbc.com.ar
    openqube,adamantium,openqube.png,https://openqube.io/
    cognizant soft vision,diamond,cognizantsoftvision.png,https://sysar.my/cognizantsoftvision
    google cloud platform,adamantium,googlecloud.png,https://cloud.google.com/
    rappi,silver,rappi.png,https://rappi.io/

    ###########################

    Returns:
        flask.Response: The rendered sponsors HTML template.
    """
    # FIXME: Add error handling
    # Get the configuration from the config file
    sponsors_config = read_json_file(SPONSORS_CONFIG_FILE)
    featured_categories = sponsors_config["featured_categories"]
    category_order = sponsors_config["category_order"]

    # Get a list of dictionaries based on the sponsors CSV file
    sponsors = csv_to_list_of_dicts(SPONSORS_FILE)

    # Removes trailing whitespace from the keys
    sponsors = remove_trailing_whitespace(sponsors)
    print(sponsors)
    # Convert key values to lowercase, just in case the input in the CSV is in caps
    convert_key_values_to_lowercase(sponsors, "category")

    # Sort the sponsors by the category_order list
    sponsors = sorted(
        sponsors,
        key=lambda x: category_order.index(x["category"])
        if x["category"] in category_order
        else len(category_order),
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

    ],
    "silver": [
        {
            "name": "openqube",
            "category": "silver",
            "file": "openqube.png",
            "link": "https://openqube.io/",
        }
    ],
}
    """

    # Convert the sponsors into a dictionary with the sponsors grouped by category
    grouped_sponsors = {}
    for sponsor in sponsors:
        category = sponsor["category"]
        if category in grouped_sponsors:
            grouped_sponsors[category].append(sponsor)
        else:
            grouped_sponsors[category] = [sponsor]
    # Render the template
    return render_template(
        "sponsors.html",
        title="Sponsors",
        grouped_sponsors=grouped_sponsors,
        featured_categories=featured_categories,
    )


@app.route("/code_of_conduct")
def code_of_conduct():
    """
    Shows the code of conduct page

    Returns:
        flask.Response: The rendered code of conduct HTML template.
    """
    return render_template("code_of_conduct.html", title="Code of Conduct")


@app.route("/agenda")
def agenda():
    agenda = read_json_file(AGENDA_FILE)
    return render_template("agenda.html", title="Agenda", agenda=agenda)


# TODO: Start using the embed contact form
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
