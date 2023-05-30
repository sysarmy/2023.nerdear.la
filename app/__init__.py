from flask import Flask


app = Flask(__name__)

from app import filters
from app import routes
