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

### How does the `templates/` directory work

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
