# -*- coding: UTF-8 -*-
from flask import Flask
from config import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db, User
from app.urls import indexBlueprint


def createApp():
    app = Flask(
        __name__,
        template_folder=config["Default"].TEMPLATE_FOLDER,
        static_folder=config["Default"].STATIC_FOLDER,
    )
    app.config.from_object(config["Default"])
    return app


# 实例化app
app = createApp()

# 数据库配置
db.init_app(app=app)
migrate = Migrate(app=app, db=db)

# 蓝图
app.register_blueprint(indexBlueprint)

# session

# 命令行
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)

# 启动实例
if __name__ == "__main__":
    manager.run()
