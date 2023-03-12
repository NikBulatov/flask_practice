from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[validators.DataRequired(),
                                    validators.Email()])
    password = PasswordField(
        "Password",
        validators=[validators.DataRequired()])
    submit = SubmitField("Login")
