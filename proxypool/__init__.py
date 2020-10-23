# -*- coding: utf-8 -*-
from flask import  Blueprint
from flask_restful import Resource, Api


api_bp = Blueprint("api", __name__, url_prefix="/api")

