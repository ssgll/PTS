# -*- coding:utf-8 -*-
from flask import render_template
from app.forms import LoginForm, SignUpForm, AddMonitorItemForm
from app.models import db, UserInformation, UserCommodity

def indexView():
    return render_template (
        "index.html"
    )


def loginView():
    form = LoginForm ()
    return render_template (
        "login.html",
        form=form
    )


def signupView():
    form = SignUpForm ()
    return render_template (
        "sign_up.html",
        form=form
    )


def about_meView():
    return render_template (
        "about_me.html"
    )


def monitorView():
    user = db.session.query (UserInformation).one ()
    commodityList = user.usercommoditys
    return render_template (
        "monitor.html",
        user = user,
        commodityList = commodityList
    )

def addMonitorView():
    form = AddMonitorItemForm()
    return render_template(
        "add_commodity.html",
        form = form
    )