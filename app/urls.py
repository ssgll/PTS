# -*- coding: UTF-8 -*-
from app import indexBlueprint

from app.views.index import indexView
from app.views.loginAndRegister import loginView,registerView

indexBlueprint.add_url_rule('/', "index", indexView, methods=["POST", "GET"])
indexBlueprint.add_url_rule('/signin', "signin", loginView, methods=["POST", "GET"])
indexBlueprint.add_url_rule('/signup', "signup", registerView, methods=["POST", "GET"])
