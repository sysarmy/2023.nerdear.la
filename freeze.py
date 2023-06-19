"""standard freeze script"""

from flask_frozen import Freezer
from app import app

freezer = Freezer(app)


@freezer.register_generator
def en():
    yield "/en/"
    yield "/es/"


if __name__ == "__main__":
    try:
        freezer.freeze()
    except Exception as e:
        print(f"{e}")
