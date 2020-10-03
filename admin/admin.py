# -*- coding: utf-8 -*-
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from models import db
from flask_login import login_required


class AdminView:
    def __init__(self, app, modelList):
        self.admin = Admin(name="Admin")
        self.admin.init_app(app=app)
        for Models in modelList:
            self.admin.add_view(ModelView(Models, db.session))

    @login_required
    class AdminView(BaseView):
        @expose("/")
        def index(self):
            return self.render("admin.html")
