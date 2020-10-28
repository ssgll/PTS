# -*- coding: utf-8 -*-
from flask_restful import Api
from proxypool import api_bp
from proxypool.views import ProxyPoolView

api = Api(api_bp)
api.add_resource(ProxyPoolView, "/")
