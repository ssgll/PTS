# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, session
from app.forms import LoginForm, SignUpForm, AddMonitorItemForm
from app.models import db, UserInformation, UserCommodity
from flask_login import login_required, logout_user, login_user, current_user


# 主页
def indexView():
    return render_template("index.html")


# 注册
def signupView():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            userName = request.form.get("user_name")
            email = request.form.get("user_email")
            password = request.form.get("password")
            user = UserInformation(userName=userName, password=password, email=email)
            check_ = (
                db.session.query(UserInformation)
                .filter(db.or_(userName == userName, email == email))
                .first()
            )
            if check_:
                flash("用户名或邮箱已经注册")
                return redirect(url_for("indexBlueprint.signup"))
            else:
                try:
                    db.session.add(user)
                    db.session.commit()
                    logout_user(user)
                    session["user"] = user.userName
                    session["userID"] = user.id
                    return redirect(url_for("indexBlueprint.index"))
                except AttributeError as e:
                    db.session.rollback()
                    flash("服务器错误，请重试或联系网站管理员")
                    return redirect(url_for("indexBlueprint.signup"))
    return render_template("sign_up.html", form=form)


# 登录
def loginView():
    form = LoginForm()
    return render_template("login.html", form=form)


def logoutView():
    session.clear()
    logout_user()
    return redirect(url_for("indexBlueprint.index"))


# 关于我
def about_meView():
    return render_template("about_me.html")


# 监控页面
@login_required
def monitorView():
    user = db.session.query(UserInformation).one()
    commodityList = user.usercommoditys
    return render_template("monitor.html", user=user, commodityList=commodityList)


# 添加监控商品
@login_required
def addMonitorView():
    form = AddMonitorItemForm()
    return render_template("add_commodity.html", form=form)
