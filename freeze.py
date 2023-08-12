import os
from flask_frozen import Freezer
from app import app
from flask import url_for
from flask_babel import force_locale
import shutil

freezer = Freezer(app, log_url_for=False)


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


def replace_index_with_redirect():
    # Get the directory where this script is located
    # This ensures that the paths are constructed based on the script's location and not from where you run the file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to your preexisting index.html
    preexisting_index_path = os.path.join(script_dir, "index_override.html")

    # Path to build/index.html
    build_index_path = os.path.join(script_dir, "app/build/index.html")

    # Copy your preexisting index.html to build/
    shutil.copy(preexisting_index_path, build_index_path)


if __name__ == "__main__":
    freezer.freeze()
    replace_index_with_redirect()
