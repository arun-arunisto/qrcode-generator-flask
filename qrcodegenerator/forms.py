from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LinkInput(FlaskForm):
    link = StringField("Link", validators=[DataRequired()])
    submit = SubmitField("Create")