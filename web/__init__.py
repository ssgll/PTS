# -*- coding: UTF-8 -*-
from flask import Blueprint

webBlueprint = Blueprint(
    "webBlueprint",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/webBlueprint",
)
