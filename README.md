# Readme

Use black formatter for python
Dont forget to do `source env/bin/active`
Understanding Flask: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world **(READ FIRST)**

Understanding multilanguage: https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd

Jinja formatter: https://stackoverflow.com/questions/60175608/visual-studio-code-and-jinja-templates
If after associating .html files with jinja-html the icon breaks, add this to your `settings.json` (if you are using Material Icon Theme):

```json
{
	"material-icon-theme.languages.associations": {
		"jinja-html": "html"
	},
	"files.associations": {
		"*.html": "jinja-html"
	},
	"emmet.includeLanguages": {
		"jinja-html": "html"
	},
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
	"css.enabledLanguages": ["jinja-html", "django-html", "html"]
}
```
