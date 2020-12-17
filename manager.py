# -*- coding: UTF-8 -*-
from flask import Flask
from config import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db, UserInformation, UserCommodity
from flask_session import Session
from flask_login import LoginManager
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler

# app
def createApp():
    app = Flask(__name__)
    app.config.from_object(config["Default"])
    CORS(app)
    return app


# 调度器
def oneJob():
    print(1)


def migrateApp(app, db):
    # 数据库配置
    db.init_app(app=app)
    migrate = Migrate(app=app, db=db)
    return app


def registerBlueprint(app):
    # 蓝图
    from web.urls import webBlueprint
    from admin.urls import adminBlueprint
    from proxypool.urls import api_bp

    app.register_blueprint(adminBlueprint, url_prefix="/admin")
    app.register_blueprint(webBlueprint, url_prefix="/")
    app.register_blueprint(api_bp, url_prefix="/proxy")

    # 调度器
    # sche = BackgroundScheduler()
    # sche.add_job(oneJob, trigger="interval",seconds=5)
    # sche.start()
    return app


# 实例化
app = createApp()
app = migrateApp(app=app, db=db)
app = registerBlueprint(app)

# session
Session(app)

# 定时器
# celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
# celery.conf.update(app.config)

# 登录
loginManager = LoginManager()
loginManager.init_app(app=app)
loginManager.login_view = "webBlueprint.index"

# 获取登录用户
@loginManager.user_loader
def load_user(user_id):
    return UserInformation.query.get(user_id)


# 初始化admin
# modelList = (UserInformation, UserCommodity)
# AdminView(app=app, modelList=modelList)

# 命令行
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)


# 启动实例（仅调试使用
if __name__ == "__main__":
    manager.run()
