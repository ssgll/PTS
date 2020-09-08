# -*- coding: UTF-8 -*-
from flask import render_template
from app.forms import SignInForm, SignUpForm

def loginView():
    form = SignInForm()
    return render_template(
        "sign_in.html", 
        form=form
    )

def registerView(): 
    form = SignUpForm()
    return render_template(
        "sign_up.html",
        form = form
    )