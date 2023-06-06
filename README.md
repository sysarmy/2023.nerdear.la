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

## Helpful information

### helpful links

Understanding Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world **(READ FIRST)**

Understanding multilanguage: https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd

Jinja formatter: https://stackoverflow.com/questions/60175608/visual-studio-code-and-jinja-templates

Using Flask, Flask-WTF, and AJAX for forms:
If you are confused about how contact.html, submit_contact/ and contact.js work, watch this video: https://www.youtube.com/watch?v=QKcVjdLEX_s and then read this blog https://blog.carsonevans.ca/2019/08/20/validating-ajax-requests-with-wtforms-in-flask/

### recommended settings for `settings.json` in Visual Studio Code

You should add this line in your User settings.json.
The reason for that is because that specific line is not available for workspace specific configuration, which is defined in the `.vscode/settings.json` file

```json
{
	"css.enabledLanguages": ["jinja-html", "django-html", "html"]
}
```
