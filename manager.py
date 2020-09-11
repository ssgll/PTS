# -*- coding: UTF-8 -*-
from flask import Flask
from config import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db, UserInformation



def createApp():
    app = Flask(
        __name__
    )
    app.config.from_object(config["Default"])
    return app



def migrateApp(app,db):
	# 数据库配置
	db.init_app(app=app)
	migrate = Migrate(app=app, db=db)
	return app

def registerBlueprint(app):
	# 蓝图
	from app.urls import indexBlueprint

	app.register_blueprint(indexBlueprint)
	return app

# session

#实例化
app = createApp()
app = migrateApp(app=app, db=db)
app = registerBlueprint(app)

# 命令行
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)

# 启动实例（仅调试使用
if __name__ == "__main__":
    manager.run()
