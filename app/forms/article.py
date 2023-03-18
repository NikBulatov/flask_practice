from flask_wtf import FlaskForm
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     validators,
                     SelectMultipleField)


class CreateArticleForm(FlaskForm):
    title = StringField("Title", validators=[validators.DataRequired()])
    body = TextAreaField("Body", validators=[validators.DataRequired()])
    submit = SubmitField("Publish")
    tags = SelectMultipleField("Tags", coerce=int)
