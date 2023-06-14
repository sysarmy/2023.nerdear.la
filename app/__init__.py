from flask import Flask
from .logger_config import configure_logger

app = Flask(__name__)

# Configure the logger
configure_logger(app)

from app import filters
from app import routes
