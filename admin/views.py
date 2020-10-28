# -*- coding: utf-8 -*-
from models import db, UserInformation, UserCommodity
from flask import render_template, redirect, url_for, session
from math import ceil
from flask_login import current_user

PAGE_COUNT = 15


def UserInformationView(page=1):
    if current_user.is_authenticated:
        identified = (
            db.session.query(UserInformation)
            .filter(UserInformation.id == session["userID"])
            .one()
            .type
        )
    else:
        identified = False
    if identified:
        global PAGE_COUNT
        UserInformationList = (
            db.session.query(UserInformation)
            .offset((page - 1) * PAGE_COUNT)
            .limit(PAGE_COUNT)
            .all()
        )
        pageCount = ceil(len(db.session.query(UserInformation).all()) / PAGE_COUNT)
        return render_template(
            "UserInformationList.html",
            page=page,
            pageCount=pageCount,
            UserInformationList=UserInformationList,
        )
    else:
        return redirect(url_for("webBlueprint.index"))


def UserCommodityView(page=1):
    if current_user.is_authenticated:
        identified = (
            db.session.query(UserInformation)
            .filter(UserInformation.id == session["userID"])
            .one()
            .type
        )
        print(current_user.id)
    else:
        identified = False
    print(identified)
    if identified:
        global PAGE_COUNT
        UserCommodityList = (
            db.session.query(UserCommodity)
            .offset((page - 1) * PAGE_COUNT)
            .limit(PAGE_COUNT)
            .all()
        )
        pageCount = ceil(len(db.session.query(UserCommodity).all()) / PAGE_COUNT)
        return render_template(
            "UserCommodityList.html",
            page=page,
            UserCommodityList=UserCommodityList,
            pageCount=pageCount,
        )
    else:
        return redirect(url_for("webBlueprint.index"))
