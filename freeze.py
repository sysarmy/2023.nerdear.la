from flask_frozen import Freezer
from app import app

app.config["FREEZER_BASE_URL"] = "/2023.nerdear.la/"

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
