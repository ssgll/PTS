# -*- coding: UTF-8 -*-
from app import indexBlueprint

from app.views.index import indexView
from app.views import index, about_me, iot2012, twitter, login, sign_up, deleteitem, offitem

indexBlueprint.add_url_rule("/", "index", index, methods=["POST", "GET"])
indexBlueprint.add_url_rule("index", "index", index, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/index.html", "index", index, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/about-me", "aboutme", about_me, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/iot2012", "iot2012", iot2012, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/twitter", "twitter", twitter, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/login", "login", login, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/sign-up", "signup", sign_up, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/deleteitem/<int:user_id>/<int:item_url>", "deleteitem", deleteitem, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/offitem/<int:user_id>/<int:item_url>", "offitem", offitem, methods=["POST", "GET"])
indexBlueprint.add_url_rule("/offitem/<int:user_id>/<int:item_url>", "offitem", offitem, methods=["POST", "GET"])
indexBlueprint.add_url_rule('/user/<int:user_id>', methods=["POST", "GET"])