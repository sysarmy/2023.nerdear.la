from flask import Flask, request, session
from .logger_config import configure_logger
from flask_babel import Babel

app = Flask(__name__)

# Configure the logger
configure_logger(app)

# Initialize babel https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n
babel = Babel(app)
from app import filters
from app import routes

app.config["LANGUAGES"] = {
    "en": "English",
    "es": "Español",
}


def get_locale():
    if "language" in session:
        return session["language"]
    return request.accept_languages.best_match(["en", "es"])


babel.init_app(app, locale_selector=get_locale)
