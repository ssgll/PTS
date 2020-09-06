# -*- coding: UTF-8 -*-
from app import indexBlueprint

from app.views.index import indexView
from app.views.login import loginView

indexBlueprint.add_url_rule('/', "index", indexView, methods=["POST", "GET"])
indexBlueprint.add_url_rule('/login', "login", loginView, methods=["POST", "GET"])
