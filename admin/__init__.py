# -*- coding: utf-8 -*-

from flask import Blueprint


adminBlueprint = Blueprint(
    "adminBlueprint",
    __name__,
    static_folder="static",
    template_folder="templates",
    static_url_path="/adminBlueprint",
)
