from app import app
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

from app.classes.DatasetsUtils import DatasetsUtils as Datasets
from app.classes.SponsorProcessor import SponsorProcessor

FAQ_FILE = "datasets/faq.json"
AGENDA_FILE = "datasets/agenda.json"
SPONSORS_FILE = "datasets/sponsors.csv"
SPONSORS_CONFIG_FILE = "datasets/sponsors_config.json"

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
    accordion_dataset = Datasets.read_json_file(FAQ_FILE)
    config = Datasets.read_json_file(SPONSORS_CONFIG_FILE)
    sponsors = Datasets.csv_to_list_of_dicts(SPONSORS_FILE)
    sponsors = SponsorProcessor.process_sponsors(sponsors, config)

    # Render the template
    return render_template(
        "index.html",
        title="Home",
        accordion_dataset=accordion_dataset,
        grouped_sponsors=sponsors,
        featured_categories=config["featured_categories"],
        featured_categories_only=True,
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

    # Get a list of dictionaries based on the sponsors CSV file
    config = Datasets.read_json_file(SPONSORS_CONFIG_FILE)
    sponsors = Datasets.csv_to_list_of_dicts(SPONSORS_FILE)
    sponsors = SponsorProcessor.process_sponsors(sponsors, config)

    # Render the template
    return render_template(
        "sponsors.html",
        title="Sponsors",
        grouped_sponsors=sponsors,
        featured_categories=config["featured_categories"],
        featured_categories_only=False,
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
    agenda = Datasets.read_json_file(AGENDA_FILE)
    return render_template("agenda.html", title="Agenda", agenda=agenda)
