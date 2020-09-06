# -*- coding: UTF-8 -*-
from flask import render_template
from app.forms import LoginForm

def loginView():
    form = LoginForm()
    return render_template("login.html", form=form)