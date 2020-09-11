# -*- coding: UTF-8 -*-
from app import indexBlueprint

from app.views import indexView, loginView, signupView, about_meView, monitorView, addMonitorView

# index
indexBlueprint.add_url_rule ("/", endpoint="index", view_func=indexView, methods=["POST", "GET"])
indexBlueprint.add_url_rule ("/index", endpoint="index", view_func=indexView, methods=["POST", "GET"])
indexBlueprint.add_url_rule ("/index.html", endpoint="index", view_func=indexView, methods=["POST", "GET"])
# login
indexBlueprint.add_url_rule ("/login", endpoint="login", view_func=loginView, methods=["POST", "GET"])
# signup
indexBlueprint.add_url_rule ("/signup", endpoint="signup", view_func=signupView, methods=["POST", "GET"])
# about me,先不要
# indexBlueprint.add_url_rule ("/about_me", endpoint="about_me", view_func=about_meView, methods=["POST", "GET"])
# monitor
indexBlueprint.add_url_rule ("/monitor", endpoint="monitor", view_func=monitorView, methods=["POST", "GET"])
# addMonitor
indexBlueprint.add_url_rule ("/addmonitor", endpoint="addmonitor", view_func=addMonitorView, methods=["POST", "GET"])


# indexBlueprint.add_url_rule("/about-me", "aboutme", about_me, methods=["POST", "GET"])
# indexBlueprint.add_url_rule("/iot2012", "iot2012", iot2012, methods=["POST", "GET"])
# indexBlueprint.add_url_rule("/twitter", "twitter", twitter, methods=["POST", "GET"])

# indexBlueprint.add_url_rule("/deleteitem/<int:user_id>/<int:item_url>", "deleteitem", deleteitem, methods=["POST", "GET"])
# indexBlueprint.add_url_rule("/offitem/<int:user_id>/<int:item_url>", "offitem", offitem, methods=["POST", "GET"])
# indexBlueprint.add_url_rule("/offitem/<int:user_id>/<int:item_url>", "offitem", offitem, methods=["POST", "GET"])
# indexBlueprint.add_url_rule('/user/<int:user_id>', methods=["POST", "GET"])
