# -*- coding: utf-8 -*-
from models import db, UserInformation, UserCommodity
from flask import render_template, redirect, url_for, session, request, jsonify
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
    else:
        identified = False
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


def commUpdate():
    try:
        data = request.get_json()
        commodityID = data["commodityID"]
        userID = data["userID"]
        commodityName = data["commodityName"]
        hopePrice = data["hopePrice"]
        status = data["status"]
        remark = data["remark"]
        nowPage = data["now_page"]
        commodity = UserCommodity(userID=userID, commodityName=commodityName)
        commodity.hopePrice = hopePrice
        commodity.status = status
        commodity.remark = remark
        del data["userID"]
        del data["now_page"]
        db.session.query(UserCommodity).filter(
            UserCommodity.commodityID == commodityID
        ).update(data)
        db.session.commit()
        return redirect(url_for("adminBlueprint.UserCommodity", page=nowPage))
        msg = {"msg":"200"}
        return jsonify(msg),200
    except Exception as e:
        return {"message": "error!"}, 404
