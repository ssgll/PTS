# -*- coding: UTF-8 -*-
from flask import Flask
from config import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, UserInformation, UserCommodity
from flask_session import Session
from flask_login import LoginManager
from admin.admin import AdminView


# app
def createApp():
    app = Flask(__name__)
    app.config.from_object(config["Development"])
    return app


def migrateApp(app, db):
    # 数据库配置
    db.init_app(app=app)
    migrate = Migrate(app=app, db=db)
    return app


def registerBlueprint(app):
    # 蓝图
    from web.urls import webBlueprint

    app.register_blueprint(webBlueprint)
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
loginManager.login_view = "webBlueprint.index"


# 获取登录用户
@loginManager.user_loader
def load_user(user_id):
    return UserInformation.query.get(int(user_id))


# 初始化admin
modelList = (UserInformation, UserCommodity)
AdminView(app=app, modelList=modelList)

# 命令行
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)


# 启动实例（仅调试使用
if __name__ == "__main__":
    manager.run()
