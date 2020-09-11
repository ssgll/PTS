# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from app.generate import GenerateId
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy ()


# 用户基本信息表
class UserInformation (db.Model):
    __table_name__ = "user_information"

    __table_args__ = {
        "mysql_charset": "utf8",
        "comment": "用户基本信息表",
    }

    id = db.Column (db.String (50), primary_key=True, index=True, comment="用户唯一标识符")
    userName = db.Column (db.String (2000), nullable=False, comment="用户名")
    name = db.Column (db.String (2000), comment="用户姓名")
    birthDate = db.Column (db.String (2000), comment="出生日期")
    telephone = db.Column (db.String (2000), comment="电话号码")
    email = db.Column (db.String (2000), comment="Email")
    passwordHash = db.Column (db.String (2000), comment="密码哈希值（不直接保存明文密码）")
    status = db.Column (db.String (2000), default="0000", comment="用户状态 0000激活 0001未激活 0010禁用")
    remark = db.Column (db.String (2000), comment="备注")

    # 禁止直接访问明文密码
    @property
    def password(self):
        raise AttributeError ("Password is not READABLE!")

    # 加密
    @password.setter
    def password(self, password):
        self.passwordHash = generate_password_hash (password)

    # 定义初始数据集
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.id = GenerateId ().next_id ()

    # 没啥用，就好看
    def __repr__(self):
        return "<username:{}>".format (self.userName)


# 用户商品表
class UserCommodity (db.Model):
    __table_name__ = "user_commodity"

    __table_args__ = {
        "mysql_charset": "utf8",
        "comment": "用户商品表",
    }

    commodityID = db.Column (db.String (50), primary_key=True, index=True, comment="商品唯一标识符")
    userID = db.Column (db.String (50), db.ForeignKey ("user_information.id"), comment="用户唯一标识符")
    commodityName = db.Column(db.String(2000), comment="商品名称")
    hopePrice = db.Column (db.String (2000), comment="期望价格")
    status = db.Column (db.String (50), default="0000", comment="商品状态 0000有效 0001无效 0010中止 0011删除")
    remark = db.Column (db.String (2000), comment="备注")

    user_fk = db.relationship ("UserInformation", backref=db.backref ("usercommoditys"))

    def __init__(self, userID, commodityName):
        self.userID = userID
        self.commodityName = commodityName
        self.commodityID = GenerateId ().next_id ()


    def __repr__(self):
        return "<userID:{}>\t<commodityName:{}>".format (self.userID, self.commodityName)
