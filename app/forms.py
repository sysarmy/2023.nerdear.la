from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    # Todo: Agregar mensajes de validacion personalizados
    name = StringField("Nombre", validators=[DataRequired()])
    surname = StringField("Apellido", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
