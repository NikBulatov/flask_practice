from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


class RegisterForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField("Email",
                        validators=[validators.DataRequired(),
                                    validators.Email()])
    password = PasswordField(
        "Password",
        validators=[
            validators.Length(8, ),
            validators.DataRequired(),
            validators.EqualTo(
                "confirm_password",
                message="Field must be equal to confirm password")
        ])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[validators.Length(8, ),
                                                 validators.DataRequired()])
    submit = SubmitField("Register")
