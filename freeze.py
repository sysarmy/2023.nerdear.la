"""standard freeze script"""

from flask_frozen import Freezer
from app import app

freezer = Freezer(app, log_url_for=False)


@freezer.register_generator
def index():
    yield "/en/"
    yield "/es/"


@freezer.register_generator
def agenda():
    yield "/en/agenda/"
    yield "/es/agenda/"


@freezer.register_generator
def sponsors():
    yield "/en/sponsors/"
    yield "/es/sponsors/"


@freezer.register_generator
def code_of_conduct():
    yield "/en/code_of_conduct/"  # Replace with the actual URL of the code of conduct endpoint
    yield "/es/code_of_conduct/"  # Replace with the actual URL of the code of conduct endpoint


if __name__ == "__main__":
    freezer.freeze()
