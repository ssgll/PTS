# -*- coding: UTF-8 -*-
from flask import Flask
from config import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db, UserInformation, UserCommodity
from flask_session import Session
from flask_login import LoginManager
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


# app
def createApp():
    app = Flask(__name__)
    app.config.from_object(config["Default"])
    return app


def migrateApp(app, db):
    # 数据库配置
    db.init_app(app=app)
    migrate = Migrate(app=app, db=db)
    return app


def registerBlueprint(app):
    # 蓝图
    from app.urls import indexBlueprint

    app.register_blueprint(indexBlueprint)
    return app


# 实例化
app = createApp()
app = migrateApp(app=app, db=db)
app = registerBlueprint(app)

# session
Session(app)

# 登录
loginManager = LoginManager()
loginManager.init_app(app=app)
loginManager.login_view = "indexBlueprint.index"


# 获取登录用户
@loginManager.user_loader
def load_user(user_id):
    return UserInformation.query.get(int(user_id))


# 初始化admin
admin = Admin(name="monitorProject")
admin.init_app(app=app)


# 添加admin界面
class AdminView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin.html")


# 实例化界面
admin.add_view(ModelView(UserInformation, db.session))
admin.add_view(ModelView(UserCommodity, db.session))

# 命令行
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)

# 启动实例（仅调试使用
if __name__ == "__main__":
    manager.run()
