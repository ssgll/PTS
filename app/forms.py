# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    PasswordField,
    TextAreaField,
    SubmitField,
    IntegerField,
)
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp


# 注册表单
class SignUpForm(FlaskForm):
    user_name = StringField(
        "user name",
        validators=[
            DataRequired(message="用户名不能为空"),
            Length(5,15, message="用户名在5-15个字之间"),
            Regexp("^[A-Za-z][A-Za-z0-9_.]*$", message="用户名只能由字母数字和下划线组成"),
        ],
    )
    user_email = StringField(
        "user email",
        validators=[
            Email(message="邮箱格式错误"),
            DataRequired(message="邮箱不能为空"),
            Length(max=128),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired(message="必须填写密码")])
    confim_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="用户名不能为空"),
            EqualTo("password", message="两次密码不一致"),
        ],
    )
    submit = SubmitField("register")


class LoginForm(FlaskForm):
    user_name = StringField(
        "user name",
        validators=[
            DataRequired(message="用户名不能为空"),
            Length(5, 15, message="用户名在5-15个字之间"),
        ],
    )
    remember_me = BooleanField("remember me", default=False)
    password = PasswordField("Password", validators=[DataRequired(message="必须填写密码")])
    submit = SubmitField("log in")


class AboutMeForm(FlaskForm):
    describe = TextAreaField("about me", validators=[DataRequired(), Length(max=140)])
    submit = SubmitField("YES!")


class AddMonitorItemForm(FlaskForm):
    commodityName = StringField("Commodity name", validators=[DataRequired()])
    hopePrice = IntegerField("Hope price", validators=[DataRequired()])
    submit = SubmitField("Add monitor")
