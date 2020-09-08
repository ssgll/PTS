# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange, Email


class SignInForm(FlaskForm):
    user_name = StringField("user name", validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField("remember me", default=False)
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("登录")


class SignUpForm(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[Email(), DataRequired(), Length(max=128)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('注册')
