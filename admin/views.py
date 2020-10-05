# -*- coding: utf-8 -*-
from models import db, UserInformation, UserCommodity
from flask import render_template


def UserinformationView():
    UserInformationList = db.session.query(UserInformation).all()
    return render_template("UserInformationList.html", UserInformationList=UserInformationList)


def UserCommodityView():
    UserCommodityList = db.session.query(UserCommodity).all()
    return render_template("UserCommodityList.html", UserCommodityList=UserCommodityList)