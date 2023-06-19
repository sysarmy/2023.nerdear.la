from flask import Flask, request
from .logger_config import configure_logger
from flask_babel import Babel

app = Flask(__name__)

# Configure the logger
configure_logger(app)

# Initialize babel https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n
LANGUAGES = ["en", "es"]
babel = Babel(app)
from app import filters
from app import routes


def get_locale():
    # return request.accept_languages.best_match(LANGUAGES)
    return "en"


babel.init_app(app, locale_selector=get_locale)
