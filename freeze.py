from flask_frozen import Freezer
from app import app
from flask import url_for
from flask_babel import force_locale

app.config["FREEZER_BASE_URL"] = "/2023.nerdear.la/"

freezer = Freezer(app, log_url_for=False)


@freezer.register_generator
def redirect_index():
    yield url_for("redirect_index")


@freezer.register_generator
def index():
    for lang in ["en", "es"]:
        with force_locale(lang):
            yield url_for("index", lang_code=lang)


@freezer.register_generator
def code_of_conduct():
    for lang in ["en", "es"]:
        with force_locale(lang):
            yield url_for("code_of_conduct", lang_code=lang)


@freezer.register_generator
def sponsors():
    for lang in ["en", "es"]:
        with force_locale(lang):
            yield url_for("sponsors", lang_code=lang)


if __name__ == "__main__":
    freezer.freeze()
