# Readme

This is the repository for Nerdearla, the Sysarmy event

## How to configure the enviroment for the project

1. Install python-virtualenv
2. Create a virtual enviroment in a folder called env/
3. Source that virtual enviroment with `source /env/bin/activate`
4. Install the packages in `requirements.txt`

## How to run the project

1. Source the python virtual enviroment with `source env/bin/active`
2. Run flask with `flask run`
3. Enjoy

## Structure of the project

```python
.
└── app: # the files used for the webapp
    ├── static # static files (the css, the fonts, the images and the javascript files)
    │   ├── css # styling
    │   ├── fonts # fonts that are not in Google Fonts
    │   ├── img # images
    │   └── js # javascript code
    └── templates # jinja-html code
			└── components # jinja-html components
```

## BACKLOG

### Frontend

#### Components

- [x] Navbar
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [ ] Hero
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [ ] Final styling
- [x] About
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] Countdown
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] Nerdearla in numbers (statistics)
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [ ] Speakers
  - [ ] Basic structure and operation
  - [ ] Responsiveness
  - [ ] Final styling
- [x] Ubication
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] FAQ
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] Contact
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] Footer
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling

#### Pages

- [x] Index
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] Sponsors
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [x] Code of Conduct
  - [x] Basic structure and operation
  - [x] Responsiveness
  - [x] Final styling
- [ ] Agenda
  - [x] Basic structure and operation
  - [ ] Responsiveness
  - [ ] Final styling

### Backend

- [ ] Logging
- [ ] Error handling
  - [ ] functions.py
  - [ ] routes.py
  - [x] filters.py
- [ ] Testing
- [ ] Multilanguage support
  - [ ] en
  - [ ] es

## FAQ

### I want to change how something is displayed in the webpage!

First, try to look which component defines that part of the webpage (if you dont know how that works, see the **"How does the `templates/` directory work?"** section).

Next, try to identify if what you are trying to modify is related to **the data that is shown** (backend related, probably inside routes.py),
or **how the data is shown** (frontend related, probably inside your component or a .html file isnide templates/)

If the problem is backend related, try to look for the route that renders the template you are looking at.
For example, if you want to change how data is collected at the sponsors page, look for the definition of the `sponsors/` route

### How does the `templates/` directory work?

Every file inside `templates/` (except `base.html`) is rendered using render_template in an specific route defined in `routes.py`.
Each file inherits from `base.html`, and uses the components in `components/` using `{% include "components/component_name_here.html" %}`

**This is done for the purpose of clean and tidy code**

An example of a component could be:

```html
<!-- This file holds the section that talks about the speakers -->
<section id="speakers">
  <!-- Get the css file using jinja-html syntax -->
  <link
    rel="stylesheet"
    href="{{ url_for('static', filename='css/speakers.css') }}"
  />

  <!-- Main content of the html -->
  <div class="container">
    <h1>Nuestros speakers</h1>
    <div>
      <p>Our speakers are great because...</p>
    </div>
  </div>

  <!-- Get the javascript file using jinja-html syntax -->
  <script src="{{ url_for('static', filename='js/speakers.js') }}"></script>
</section>
```

### How does the static/css folder work?

The CSS folder has two types of .css files

#### File specific files:

Some css files are asociated to html files inside templates/ (or templates/components).
For example, `hero.css` is used in the `hero.html` component, or `sponsors.css` is used in `sponsors.html`

#### General usage files

Other files are for general usage, like `style.css`, which defines general css to be used in the whole project.

- `fonts.css` loads the fonts from static/fonts/
- `trama_backgrounds.css` defines classes for generating backgrounds using the tramas inside img/svg/tramas
- `variables.css` defines global variables, for example the Nerderla colors.

### What is inside `datasets/`?

Datasets is a folder which contains files that modify what and how data is displayed in the page.
**The purpose of this folder was to hold files that modify the webpage without needing to touch the code**

For example, the `sponsors_config.json` file sets the order in which the sponsors are displayed in `sponsors.html`, among other things.
This json file is accessed using `read_json_file()` from `functions.py`
The sponsors are defined inside `sponsors.csv`

### How are the sponsors displayed?

The sponsors are defined in `datasets/sponsors.csv`
`sponsors.csv` should look like this:

```csv
name                  ,category   ,file            ,link
cognizant             ,diamond    ,cognizant.png   ,https://sysar.my/cognizantsoftvision
icbc                  ,adamantium ,icbc.png        ,https://www.icbc.com.ar
openqube              ,adamantium ,openqube.png    ,https://openqube.io/
google cloud platform ,adamantium ,googlecloud.png ,https://cloud.google.com/
rappi                 ,silver     ,rappi.png       ,https://rappi.io/
rappi                 ,silver     ,rappi.png       ,https://rappi.io/
rappi                 ,silver     ,rappi.png       ,https://rappi.io/
```

You can use whitespaces because the `sponsors/` route automatically removes trailing whitespaces

### How can I modify the FAQ?

In the `datasets/` folder, create or modify a `faq.json` file with FAQ's like the following:

```json
[
  {
    "title": "Que es Nerdearla",
    "description": "Nerdearla es lorem ipsum bla bla bla"
  },
  {
    "title": "Cuando se hace la Nerdearla",
    "description": "La respuesta esta en tu corazon"
  },
  {
    "title": "Cúanto sale?",
    "description": "Paga Jolo"
  }
]
```

### How does the logger work?

Generated by chatGPT:
To use the logger in each file of your Flask project, you can follow these steps:

1. Create a separate file to configure the logger. Let's call it `logger_config.py`.

```python

import logging
from flask import Flask

def configure_logger(app: Flask):
    """
    Configure and return a logger instance with different handlers for console, Werkzeug logs,
    general logs, and error logs.

    This function sets up a logger with multiple handlers to direct log messages based on their
    level and source. Non-Werkzeug log messages are sent to the console, Werkzeug logs are written
    to the 'werkzeug.log' file, INFO and higher level messages are stored in the 'general.log' file,
    and ERROR and higher level messages are captured in the 'errors.log' file.

    Args:
        app (Flask): The Flask application object.

    Returns:
        logging.Logger: The configured logger instance.

    Note:
        Make sure to call this function after creating the Flask application object.
    """
    # Create a logger instance
    logger = app.logger

    # Set the log level for the logger
    logger.setLevel(logging.DEBUG)

    # Create a console handler for non-Werkzeug logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    # Disable Werkzeug logs in the console
    werkzeug_logger = logging.getLogger("werkzeug")
    werkzeug_logger.setLevel(logging.ERROR)

    # Create a file handler for Werkzeug logs
    werkzeug_handler = logging.FileHandler('werkzeug.log')
    werkzeug_handler.setLevel(logging.DEBUG)
    werkzeug_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    werkzeug_handler.setFormatter(werkzeug_formatter)
    logger.addHandler(werkzeug_handler)

    # Create a file handler for general logs (INFO and higher)
    general_handler = logging.FileHandler('general.log')
    general_handler.setLevel(logging.INFO)
    general_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    general_handler.setFormatter(general_formatter)
    logger.addHandler(general_handler)

    # Create a file handler for error logs (ERROR and higher)
    error_handler = logging.FileHandler('errors.log')
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(error_formatter)
    logger.addHandler(error_handler)

    return logger
```

2. In the `__init__.py` file of your app folder, import the `configure_logger` function from `logger_config` and call it, passing the app object.

```python

from flask import Flask
from logger_config import configure_logger

app = Flask(__name__)

# Configure the logger
configure_logger(app)

# Import routes and functions
from app import routes
from app import functions
```

3. In the other files within the app folder (`routes.py` and `functions.py` in this case), import the logger and use it as needed.

For example, in `routes.py`:

```python

from flask import request
from app import app

logger = app.logger

@app.route('/')
def index():
    logger.info('Processing index request...')
    # Your code here

```

And in `functions.py`:

```python

from app import app

logger = app.logger

def some_function():
    logger.debug('Debug message in some_function')
    # Your code here

```

By importing the app object and logger instance from `__init__.py` in each file, you can access and use the logger across different modules and files within your Flask project.

### How to use the logger inside the classes/ folder

Generated by chatGPT

To use the app logger in the classes located within the classes folder of your Flask project, you can follow these steps:

1. In the `__init__.py` file located inside the classes folder, import the logger from the `__init__.py` file of the app folder.

```python

from app import app

logger = app.logger
```

2. In the other Python files within the classes folder (`DatasetsUtils.py` and `SponsorProcessor.py`), import the logger and use it as needed.

For example, in DatasetsUtils.`py`:

```python

from classes import logger

class DatasetsUtils:
    def some_method(self):
        logger.info('This is an info message from DatasetsUtils')
        # Your code here
```

And in `SponsorProcessor.py`:

```python

from classes import logger

class SponsorProcessor:
    def some_method(self):
        logger.debug('This is a debug message from SponsorProcessor')
        # Your code here
```

By importing the logger from the app module's `__init__.py` file in the `__init__.py` file of the classes folder, you can access and use the app logger across the classes within the classes folder.

## Helpful information

### helpful links

Understanding Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world **(READ FIRST)**

Understanding multilanguage: https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd

Jinja formatter: https://stackoverflow.com/questions/60175608/visual-studio-code-and-jinja-templates

Using Flask, Flask-WTF, and AJAX for forms:
If you are confused about how contact.html, submit_contact/ and contact.js work, watch this video: https://www.youtube.com/watch?v=QKcVjdLEX_s and then read this blog https://blog.carsonevans.ca/2019/08/20/validating-ajax-requests-with-wtforms-in-flask/

Understanding logging:
https://www.youtube.com/watch?v=-ARI4Cz-awo and https://www.youtube.com/watch?v=jxmzY9soFXg

### recommended settings for `settings.json` in Visual Studio Code

You should add this line in your User settings.json.
The reason for that is because that specific line is not available for workspace specific configuration, which is defined in the `.vscode/settings.json` file

```json
{
  "css.enabledLanguages": ["jinja-html", "django-html", "html"]
}
```
