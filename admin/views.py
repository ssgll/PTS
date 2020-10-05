# -*- coding: utf-8 -*-
from models import db, UserInformation, UserCommodity
from flask import render_template
import math


def UserinformationView():
    UserInformationList = db.session.query(UserInformation).all()
    return render_template("UserInformationList.html", UserInformationList=UserInformationList)


def UserCommodityView(page=1):
    UserCommodityList = db.session.query(UserCommodity).offset((page - 1)*10).limit(10).all()
    pageCount = math.ceil(len(db.session.query(UserCommodity).all())/10)
    return render_template("UserCommodityList.html", page=page, UserCommodityList=UserCommodityList, pageCount=pageCount)