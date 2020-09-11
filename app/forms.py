# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class LoginForm(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    remember_me = BooleanField('remember me', default=False)
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('log in')


class SignUpForm(FlaskForm):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    user_email = StringField('user email', validators=[Email(), DataRequired(), Length(max=128)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('register')


class AboutMeForm(FlaskForm):
    describe = TextAreaField('about me', validators=[DataRequired(), Length(max=140)])
    submit = SubmitField('YES!')

class AddMonitorItemForm(FlaskForm):
    commodityName = StringField("Commodity name", validators=[DataRequired()])
    hopePrice = IntegerField("Hope price", validators=[DataRequired()])
    submit = SubmitField('Add monitor')