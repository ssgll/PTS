# -*- coding: UTF-8 -*-

from flask_restful import Resource
from models import Pool, db


class ProxyPoolView(Resource):
    def get(self):
        iplist = db.session.query(Pool).all()
        return iplist
