# -*- coding: UTF-8 -*-
from web import webBlueprint

from web.views import (
    indexView,
    loginView,
    signupView,
    about_meView,
    monitorView,
    addMonitorView,
    logoutView,
)

# index
webBlueprint.add_url_rule(
    "/", endpoint="index", view_func=indexView, methods=["POST", "GET"]
)
webBlueprint.add_url_rule(
    "/index", endpoint="index", view_func=indexView, methods=["POST", "GET"]
)
webBlueprint.add_url_rule(
    "/index.html", endpoint="index", view_func=indexView, methods=["POST", "GET"]
)
# login
webBlueprint.add_url_rule(
    "/login", endpoint="login", view_func=loginView, methods=["POST", "GET"]
)
# signup
webBlueprint.add_url_rule(
    "/signup", endpoint="signup", view_func=signupView, methods=["POST", "GET"]
)
# about me,先不要
# webBlueprint.add_url_rule ("/about_me", endpoint="about_me", view_func=about_meView, methods=["POST", "GET"])
# monitor
webBlueprint.add_url_rule(
    "/monitor", endpoint="monitor", view_func=monitorView, methods=["POST", "GET"]
)
# addMonitor
webBlueprint.add_url_rule(
    "/addmonitor",
    endpoint="addmonitor",
    view_func=addMonitorView,
    methods=["POST", "GET"],
)
# logout
webBlueprint.add_url_rule(
    "/logout", endpoint="logout", view_func=logoutView, methods=["POST", "GET"]
)


# webBlueprint.add_url_rule("/about-me", "aboutme", about_me, methods=["POST", "GET"])
# webBlueprint.add_url_rule("/iot2012", "iot2012", iot2012, methods=["POST", "GET"])
# webBlueprint.add_url_rule("/twitter", "twitter", twitter, methods=["POST", "GET"])

# webBlueprint.add_url_rule("/deleteitem/<int:user_id>/<int:item_url>", "deleteitem", deleteitem, methods=["POST", "GET"])
# webBlueprint.add_url_rule("/offitem/<int:user_id>/<int:item_url>", "offitem", offitem, methods=["POST", "GET"])
# webBlueprint.add_url_rule("/offitem/<int:user_id>/<int:item_url>", "offitem", offitem, methods=["POST", "GET"])
# webBlueprint.add_url_rule('/user/<int:user_id>', methods=["POST", "GET"])
