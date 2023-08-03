from app import app, babel
from flask import render_template, request, session, jsonify, redirect
from flask_babel import _, gettext
import os
from app.classes.DatasetsUtils import DatasetsUtils as Datasets, DatasetError
from app.classes.SponsorProcessor import SponsorProcessor, SponsorProcessorError


FAQ_FILE = "datasets/faq.json"
AGENDA_FILE = "datasets/agenda.json"
SPONSORS_FILE = "datasets/sponsors.csv"
SPONSORS_CONFIG_FILE = "datasets/sponsors_config.json"

# TODO: Please for the love of god change the secret key generation
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY

# Get the logger
logger = app.logger


@app.before_request
def extract_locale_from_url():
    # Extract the language code from the URL and set it as the locale
    lang_code = request.path.split("/")[1]
    if lang_code in app.config["BABEL_LANGUAGES"]:
        babel.locale = lang_code


@app.route("/")
def nolang_index():
    # Get the user's preferred language from the Accept-Language header
    accept_language = request.headers.get("Accept-Language")
    if accept_language:
        user_language = accept_language.split(",")[0].strip().split("-")[0]

        # Redirect to the appropriate language route
        if user_language == "en":
            return redirect("/en/")
        elif user_language == "es":
            return redirect("/es/")

    # Default redirection if no Accept-Language header or unsupported language
    return redirect("/en")


@app.route("/<lang_code>/")
def index(lang_code):
    """
    Shows the index page.

    Retrieves data from JSON and CSV files, processes it, and renders the index HTML template.
    If any errors occur during data retrieval or processing, appropriate error messages are logged.

    Returns:
        flask.Response: The rendered index HTML template.
    """
    sponsors_error = False
    try:
        # The data to put in the faq accordion
        accordion_dataset = Datasets.read_json_file(FAQ_FILE)
        config = Datasets.read_json_file(SPONSORS_CONFIG_FILE)
        sponsors = Datasets.csv_to_list_of_dicts(SPONSORS_FILE)
        sponsors = SponsorProcessor.process_sponsors(sponsors, config)
    except DatasetError as e:
        # Change to logger.exception if you want the whole traceback
        logger.error(f"Exception occurred: {e}")
        sponsors_error = True
    except SponsorProcessorError as e:
        logger.error(f"Exception occurred: {e}")
        sponsors_error = True
    except Exception as e:
        logger.error(f"Unexpected exception: {e}")
    # Render the template
    return render_template(
        "index.html",
        title="Home",
        accordion_dataset=accordion_dataset,
        grouped_sponsors=sponsors if not sponsors_error else None,
        featured_categories=config["featured_categories"],
        featured_categories_only=True,
        sponsors_error=sponsors_error,
        lang_code=lang_code,
    )


@app.route("/<lang_code>/sponsors/")
def sponsors(lang_code):
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
    sponsors_error = False
    try:
        config = Datasets.read_json_file(SPONSORS_CONFIG_FILE)
        sponsors = Datasets.csv_to_list_of_dicts(SPONSORS_FILE)
        sponsors = SponsorProcessor.process_sponsors(sponsors, config)
    except DatasetError as e:
        # Change to logger.exception if you want the whole traceback
        logger.error(f"Exception occurred {e}")
        sponsors_error = True
    except SponsorProcessorError as e:
        logger.error(f"Exception occurred {e}")
        sponsors_error = True
    except Exception as e:
        logger.error(f"Unexpected exception: {e}")

    # Render the template
    return render_template(
        "sponsors.html",
        title="Sponsors",
        grouped_sponsors=sponsors if not sponsors_error else None,
        featured_categories=config["featured_categories"],
        featured_categories_only=False,
        sponsors_error=sponsors_error,
        lang_code=lang_code,
    )


@app.route("/<lang_code>/code_of_conduct/")
def code_of_conduct(lang_code):
    """
    Shows the code of conduct page

    Returns:
        flask.Response: The rendered code of conduct HTML template.
    """
    return render_template("code_of_conduct.html", title="Code of Conduct", lang_code=lang_code)


# @app.route("/<lang_code>/agenda/")
# def agenda(lang_code):
#     agenda = Datasets.read_json_file(AGENDA_FILE)
#     return render_template(
#         "agenda.html",
#         title="Agenda",
#         agenda=agenda,
#         lang_code=lang_code,
#     )


# TODO: Add 404 page
