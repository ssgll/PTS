# -*- coding: utf-8 -*-
import datetime
# from string import strip
from app import app, db, lm
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Monitor, ROLE_USER
from app.forms import LoginForm, SignUpForm, AboutMeForm, AddMonitorItemForm
from app.PriceMonitor import additemcrawl
import tweepy
from sqlalchemy import and_

@app.route('/')
@app.route('/index')
@app.route('/index.html')


# def index():
# 	return "12345"
# @app.route('/')
# @app.route('/index')
#
def index():
    # item_number = Monitor.query.count()
    # user_number = User.query.count()
    return render_template("index.html", title="Home", item_number=item_number, user_number=user_number)
    # try:
    #     item_number = Monitor.query.count()
    #     user_number = User.query.count()
    # except:
    #     return render_template("index.html", title="Home")
    # return render_template("index.html", title="Home", item_number=item_number, user_number=user_number)



def about_me():
    return render_template("about_me.html", title="about me")


def iot2012():
    return render_template("iot2012.html", title="Jiangda Internet of Things")


def twitter():
    # consumer_key = "kIzG8NiFtJJKMtM8j6mjIJASm"
    # consumer_secret = "zz346qvg5beasTDC8GvUvVqYD4B7XruTez63h7OCLUD8wCYyiT"
    # access_token = '851927351831085056-Ennbtyu5E0MIrQcspvYSBuItSZdFX9i'
    # access_token_secret ='ApSomBKX2FQ4vy2r0AZrXReDVerPbmnDhL2p1KeQptXoO'
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
    # twitter_trump = api.user_timeline('realDonaldTrump')

    return render_template("twitter.html", title="Twitter", twitter_trump=twitter_trump)

def login():
    # Verify that the user is verified
    if current_user.is_authenticated:
        return redirect('index')
    # Registration verification
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        user_name = request.form.get('user_name')
        password = request.form.get('password')

        # Password validation
        try:
            user_forpwd = User.query.filter(User.nickname == user_name).first()
            print(type(user_forpwd), user_forpwd.password)
            if not check_password_hash(user_forpwd.password, password):
                flash('User name or password is wrong')
                return redirect('/login')
        except:
            flash("The user seems to have no password")
            return redirect('/login')

        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()

            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("Database read error, please try again")
                return redirect('/login')

            # flash(request.form.get('user_name'))
            # flash('remember me? '+ str(request.form.get('remember_me')))
            flash('Login successful')
            return redirect(url_for("users", user_id=current_user.id))
        else:
            flash('There is no such user, please register')
            return redirect('/login')

    return render_template("login.html", title="Sign In", form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')
        password = request.form.get('password')
        password = generate_password_hash(password)
        register_check = User.query.filter(db.or_(
            User.nickname == user_name, User.email == user_email)).first()
        if register_check:
            flash("duplicate username or email")
            return redirect('/sign-up')

        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.role = ROLE_USER
            user.password = password
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("Database read error, please try again")
                return redirect('/sign-up')

            flash("Registered successfully")
            return redirect('/login')

    return render_template("sign_up.html", form=form)


@app.route('/user/<int:user_id>', methods=["POST", "GET"])
@login_required
def users(user_id):
    form = AboutMeForm()
    user = User.query.filter(User.id == user_id).first()
    if user_id is not current_user.id:
        return redirect(url_for('index'))
    if not user:
        flash("The user is not exist.")
        redirect("/index")
    all_item = user.all_item.all()

    return render_template("user.html", form=form, user=user, all_item=all_item)


@app.route('/addmonitoritem/<int:user_id>', methods=["POST", "GET"])
@login_required
def addmonitoritem(user_id):
    form = AddMonitorItemForm()
    item = Monitor()
    if form.validate_on_submit():
        item_url = request.form.get("item_url")
        if not len(item_url.strip()):
            flash("Product ID is required")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        user_price = request.form.get("user_price")
        if not len(user_price.strip()):
            flash("The content is necessray!")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        mall_id = request.form.get("mall_id")
        if not len(item_url.strip()):
            flash("The content is necessray!")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        current_mall_id=''
        if item_url.__contains__('costco'):
            current_mall_id='1'
        elif item_url.__contains__('bhphotovideo'):
            current_mall_id = '2'
        elif item_url.__contains__('ozymart'):
            current_mall_id = '3'
        elif item_url.__contains__('aliexpress'):
            current_mall_id = '4'
        else:
            flash('This store is currently not supported.')
        if current_mall_id != mall_id:
            flash('Please choose the right store.')
            return redirect(url_for("addmonitoritem", user_id=user_id))
        item_url=item_url.strip()
        item.item_url = item_url
        item.user_price = user_price
        item.mall_id = mall_id
        item.add_date = datetime.datetime.now()
        item.user_id = user_id
        item.status = True
        try:
            item_exist = Monitor.query.filter(and_(Monitor.item_url == item_url,Monitor.user_id == user_id)).first()
            # print(item_exist)
            if item_exist is not None:
                flash("The product is already in the monitoring list")
                return redirect(url_for("addmonitoritem", user_id=user_id))
            # sql_items = "select item_url from monitor where user_id=:user_id"
            # for items in sql_items:
            #     if items==item_url:
            #         flash("The product is already in the monitoring list")
            #         return redirect(url_for("users", user_id=user_id))
        except:
            flash("Database query product error, please try again")
            return redirect(url_for("addmonitoritem", user_id=user_id))

        item_name, item_price = additemcrawl.additemcrawl(item_url, user_id, mall_id)
        print(type(item_name), type(item_price), item_name)
        # if type(item_name) == str:
        # flash("The product does not exist, please enter the correct product ID")
        # return redirect(url_for("addmonitoritem", user_id=user_id))

        item.item_name = item_name
        item.item_price = item_price

        try:
            db.session.add(item)
            db.session.commit()
        except:
            flash("error writing to database")
            return redirect(url_for("addmonitoritem", user_id=user_id))
        flash("Add product successfully")
        return redirect(url_for("users", user_id=user_id))

    return render_template("addmonitoritem.html", form=form)


@app.route('/deleteitem/<int:user_id>/<int:item_url>', methods=["POST", "GET"])
@login_required
def delete_item(item_url, user_id):
    try:
        db.session.query(Monitor).filter_by(id=item_url).delete()
        db.session.commit()
    except:
        flash("Database read error, please try again")
        return redirect(url_for("users", user_id=user_id))
    return redirect(url_for("users", user_id=user_id))


# @app.route('/onitem/<int:user_id>/<int:item_url>', methods=["POST", "GET"])
@login_required
def on_item(item_url, user_id):
    try:
        db.session.query(Monitor).filter_by(id=item_url).update({"status": True})
        db.session.commit()
    except:
        flash("Database read error, please try again")
        return redirect(url_for("users", user_id=user_id))
    return redirect(url_for("users", user_id=user_id))


# @app.route('/offitem/<int:user_id>/<int:item_url>', methods=["POST", "GET"])
@login_required
def off_item(item_url, user_id):
    try:
        db.session.query(Monitor).filter_by(id=item_url).update({"status": False})
        db.session.commit()
    except:
        flash("Database read error, please try again")
        return redirect(url_for("users", user_id=user_id))
    return redirect(url_for("users", user_id=user_id))