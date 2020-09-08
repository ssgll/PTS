# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from app.generate import GenerateId
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# 用户基本信息表
class UserInformation(db.Model):
    __table_name__ = "user_information"

    id = db.Column(db.String(50), primary_key=True, index=True, comment="用户唯一标识符")
    userName = db.Column(db.String(2000), nullable=False, comment="用户名")
    name = db.Column(db.String(2000), comment="用户姓名")
    birthDate = db.Column(db.String(2000), comment="出生日期")
    telephone = db.Column(db.String(2000), comment="电话号码")
    email = db.Column(db.String(2000), comment="Email")
    passwordHash = db.Column(db.String(2000), comment="密码哈希值（不直接保存明文密码）")
    status = db.Column(db.String(2000), comment="用户状态 1、激活 2、未激活 3、禁用")
    remark = db.Column(db.String(2000), comment="备注")

    __table_args__ = {
        "mysql_charset": "utf8",
        "comment": "用户基本信息表",
    }

    # 禁止直接访问明文密码
    @property
    def password(self):
        raise AttributeError("Password is not READABLE!")

    # 加密
    @password.setter
    def password(self, password):
        self.passwordHash = generate_password_hash(password)

    # 定义初始数据集
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.id = GenerateId().next_id()

    # 没啥用，就好看
    def __str__(self):
        return "<username:{}>".format(self.username)
