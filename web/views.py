# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, session
from web.forms import LoginForm, SignUpForm, AddMonitorItemForm
from models import db, UserInformation
from flask_login import login_required, logout_user, login_user, current_user
from werkzeug.security import check_password_hash


# 主页
def indexView():
    if not session.get("user"):
        redirect(url_for("webBlueprint.login"))
    return render_template("index.html")


# 注册
def signupView():
    form = SignUpForm()
    # 接受返回的数据
    if request.method == "POST":
        if form.validate_on_submit():
            userName = request.form.get("user_name")
            email = request.form.get("user_email")
            password = request.form.get("password")
            user = UserInformation(userName=userName, password=password, email=email)
            # 查看是否已经注册
            check_ = (
                db.session.query(UserInformation)
                .filter(
                    db.or_(
                        UserInformation.userName == userName,
                        UserInformation.email == email,
                    )
                )
                .first()
            )
            if check_ is not None:
                flash("用户名或邮箱已经注册")
                return redirect(url_for("webBlueprint.signup"))
            else:
                try:
                    # 校验成功，写入 ，并跳转到主页，获取到session
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    session["user"] = user.userName
                    session["userID"] = user.id
                    return redirect(url_for("webBlueprint.index"))
                except AttributeError as e:
                    flash(e)
                    return redirect(url_for("webBlueprint.signup"))
    return render_template("sign_up.html", form=form)


# 登录
def loginView():
    form = LoginForm()
    # 判断用户是否已经登录
    if current_user.is_authenticated:
        redirect(url_for("webBlueprint.index"))
    if request.method == "POST":
        userName = request.form.get("user_name")
        password = request.form.get("password")

        try:
            user = (
                db.session.query(UserInformation)
                .filter(UserInformation.userName == userName)
                .first()
            )
            passwordHash = user.passwordHash
            if check_password_hash(passwordHash, password):
                login_user(user)
                session["user"] = user.userName
                session["userID"] = user.id
                return redirect(url_for("webBlueprint.index"))
            else:
                flash("密码错误，请重试")
                return redirect(url_for("webBlueprint.login"))
        except AttributeError as e:
            flash("用户不存在")
            return redirect(url_for("webBlueprint.login"))
    return render_template("login.html", form=form)


@login_required
def logoutView():
    session.clear()
    logout_user()
    return redirect(url_for("webBlueprint.index"))


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
