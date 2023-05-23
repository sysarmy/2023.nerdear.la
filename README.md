# Readme

This is the repository for Nerdearla, the Sysarmy event

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
    │   │   └── RiftSoft
    │   ├── img # images
    │   │   └── logos
    │   └── js # javascript code
    └── templates # jinja-html code, divided into several parts
```

### How does the `templates/` directory work

Every file inside `templates/` (except `base.html`) is included inside the body of `base.html`, for example:

```jinja-html
<body>
	{% include "navbar.html" %} {# Navbar #}
	{% include "hero.html" %} {# Hero with the title and a CTA #}
	{% include "about.html" %} {# About section with introductory info about the event #}
	{% include "countdown.html" %} {# Countdown till the start of the event #}
	{% include "statistics.html" %} {# Nerdearla in numbers (atendees, n of speakers, sponsors, exhibitors, etc...) #}
	{% include "speakers.html" %} {# About the speakers #}
	{% include "ubication.html" %} {# Google maps iframe #}
	{% include "sponsors.html" %} {# Sponsors of Nerdearla #}
	{% include "faq.html" %} {# This generates the FAQ #}
	{% include "contact.html" %} {# Contact form like https://productschool.com/productcon/london-2024 #}
	{% include "footer.html" %} {# Footer #}
	{# Load Bootstrap JS#}
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"
		integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous">
		</script>
</body>
```

**This is done for the purpose of clean and tidy code**

An example of an included file could be:

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

Use black formatter for python
Understanding Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world **(READ FIRST)**

Understanding multilanguage: https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd

Jinja formatter: https://stackoverflow.com/questions/60175608/visual-studio-code-and-jinja-templates

### recommended settings for `settings.json` in Visual Studio Code

```json
{
	// If after associating .html files with jinja-html the icon breaks, add this to your `settings.json` (if you are using Material Icon Theme):
	"material-icon-theme.languages.associations": {
		"jinja-html": "html"
	},
	// Associate jinja-html with html
	"files.associations": {
		"*.html": "jinja-html"
	},
	// Add support for emmet in jinja-html
	"emmet.includeLanguages": {
		"jinja-html": "html"
	},
	// Add jinja-html to css class completion extension
	"html-css-class-completion.HTMLLanguages": [
		"jinja-html",
		"html",
		"vue",
		"razor",
		"blade",
		"handlebars",
		"twig",
		"django-html",
		"php",
		"markdown",
		"erb",
		"ejs",
		"svelte"
	],
	// Add jinja-html to css extension
	"css.enabledLanguages": ["jinja-html", "django-html", "html"]
}
```
