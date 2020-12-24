# -*- coding:utf-8 -*-
from flask import render_template, redirect, url_for, request, flash, session, render_template_string, jsonify
from web.forms import LoginForm, SignUpForm, AddMonitorItemForm, UserinformationChangeForm
from models import db, UserInformation, UserCommodity
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
                print(session["userID"])
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
    user = (
        db.session.query(UserInformation)
        .filter(UserInformation.id == current_user.id)
        .one()
    )
    commodityList = user.usercommoditys
    return render_template("monitor.html", user=user, commodityList=commodityList)


# 添加监控商品
@login_required
def addMonitorView():
    form = AddMonitorItemForm()
    if request.method == "POST":
        commodityName = request.form.get("commodityName")
        hopePrice = request.form.get("hopePrice")
        user_id = current_user.id
        count = len(
            db.session.query(UserCommodity)
            .filter(UserCommodity.userID == user_id, UserCommodity.status == "0000")
            .all()
        )
        if count >= 10:
            flash("最多添加10条有效记录,请重试")
        else:
            commodity = UserCommodity(userID=user_id, commodityName=commodityName)
            commodity.hopePrice = hopePrice
            try:
                db.session.add(commodity)
                db.session.commit()
                return redirect(url_for("webBlueprint.monitor"))
            except Exception as e:
                flash("服务器错误，请重试")
                return redirect(url_for("webBlueprint.addmonitor", form=form))
    return render_template("add_commodity.html", form=form)


# 状态改变
@login_required
def monitorChange(commodityID, status):
    count = len(
        db.session.query(UserCommodity)
        .filter(UserCommodity.userID == current_user.id, UserCommodity.status == "0000")
        .all()
    )
    if count >= 10:
        flash("最多添加10条有效记录,请重试")
        return redirect(url_for("webBlueprint.monitor"))
    elif status == "0000" or status == "0010":
        status = "0000" if status == "0010" else "0010"
        try:
            db.session.query(UserCommodity).filter(
                UserCommodity.userID == current_user.id,
                UserCommodity.commodityID == commodityID,
            ).update({"status": status})
            db.session.commit()
            return redirect(url_for("webBlueprint.monitor"))
        except Exception as e:
            return {"msg": "error!"}, 404


# 删除
@login_required
def commChange(commodityID):
    try:
        db.session.query(UserCommodity).filter(
            UserCommodity.userID == current_user.id,
            UserCommodity.commodityID == commodityID,
        ).delete()
        db.session.commit()
        return redirect(url_for("webBlueprint.monitor"))
    except Exception as e:
        return {"msg": "error!"}, 404


# 用户信息修改
@login_required
def userInformationChange():
    user = db.session.query(UserInformation).filter(UserInformation.id == current_user.id).one()
    form = UserinformationChangeForm(username=user.userName,name=user.name,telephone=user.telephone,Email=user.email)
    if request.method == "POST" and form.validate_on_submit():
        new_data = {
            "userName": request.form.get("username"),
            "birthDate": request.form.get("birthDay"),
            "telephone": request.form.get("telephone"),
            "name": request.form.get("name"),
            "email": request.form.get("Email"),
        }
        try:
            db.session.query(UserInformation).filter(UserInformation.id == current_user.id).update(new_data)
            db.session.commit()
            return render_template("replace.html")
        except Exception as e:
            return jsonify({"message":"error!"}),404

    return render_template("usreInformationChange.html", form=form)
