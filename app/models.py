# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
import time
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# 用户基本信息表
class User(db.Model):
    __table_name__ = "user"
    __table_args__ = {
        "mysql_charset": "utf8"
    }

    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(2000),nullable=False)
    name = db.Column(db.String(2000))
    birth = db.Column(db.String(2000))
    telephone = db.Column(db.String(2000))
    email = db.Column(db.String(2000))
    password_hash = db.Column(db.String(2000))
    status = db.Column(db.String(2000)) # 用户状态 1、激活  2、未激活
    remark = db.Column(db.String(2000))

    # 禁止直接访问明文密码
    @property
    def password(self):
        raise AttributeError("Password is not READABLE!")

    # 加密
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 定义初始数据集
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = int(time.time())

    # 没啥用，就好看
    def __str__(self):
        return "<username:{}>".format(self.username)