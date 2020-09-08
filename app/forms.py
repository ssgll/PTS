# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class LoginForm(FlaskForm):
    user_name = StringField("user name", validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField("remember me", default=False)
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("登录")