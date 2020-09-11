# -*- coding: UTF-8 -*-
from flask import Blueprint
from config import config
config = config["Default"]


indexBlueprint = Blueprint('indexBlueprint',__name__,template_folder="templates",static_folder="static",static_url_path="/app/static")