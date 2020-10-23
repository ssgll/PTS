# -*- coding: UTF-8 -*-
import os
import redis
import pymysql
from datetime import timedelta


class Config:
    # 调试信息
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True

    # 数据库信息
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_USER = "ssgll"
    DB_PASSWORD = "guojian"
    DB_NAME = "pts"
    DB_CHARSET = "utf8"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_CHARSET
    )
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # 根目录 模板 静态文件
    BASE_DIR = os.getcwd()
    APP_TEMPLATE_FOLDER = os.path.join(BASE_DIR, "app/templates")
    APP_STATIC_FOLDER = os.path.join(BASE_DIR, "app/static")
    STATIC_URL_PATH = os.path.join(BASE_DIR, "app/static")

    # Session配置
    SECRET_KEY = "OO0ryy#Z2OcySOBpP6OTen*oeuqq8BxE"
    SESSION_TYPE = "redis"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "383687"
    REDIS_POOL = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
    )
    SESSION_REDIS = redis.Redis(connection_pool=REDIS_POOL)
    SESSION_USE_SIGNER = False
    SESSION_KEY_PREFIX = "session:"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)

    # 定时器
    CELERY_BROKER_URL = 'redis://:383687@127.0.0.1:6379/1'
    CELERY_RESULT_BACKEND = 'redis://:383687@127.0.0.1:6379/1'

class Development(Config):
    # 调试信息
    HOST = "0.0.0.0"
    PORT = 5000
    DEBUG = True

    # 数据库信息
    DB_HOST = "172.19.0.4"
    DB_PORT = 3306
    DB_USER = "ssgll"
    DB_PASSWORD = "383687"
    DB_NAME = "pts"
    DB_CHARSET = "utf8"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, DB_CHARSET
    )
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # 根目录 模板 静态文件
    BASE_DIR = os.getcwd()
    APP_TEMPLATE_FOLDER = os.path.join(BASE_DIR, "app/templates")
    APP_STATIC_FOLDER = os.path.join(BASE_DIR, "app/static")
    STATIC_URL_PATH = os.path.join(BASE_DIR, "app/static")

    # Session配置
    SECRET_KEY = "OO0ryy#Z2OcySOBpP6OTen*oeuqq8BxE"
    SESSION_TYPE = "redis"
    REDIS_HOST = "172.19.0.3"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "383687"
    REDIS_POOL = redis.ConnectionPool(
        host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
    )
    # REDIS_POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_REDIS = redis.Redis(connection_pool=REDIS_POOL)
    SESSION_USE_SIGNER = False
    SESSION_KEY_PREFIX = "session:"
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)

    # 定时器
    CELERY_BROKER_URL = 'redis://:383687@127.0.0.1:6379/1'
    CELERY_RESULT_BACKEND = 'redis://:383687@127.0.0.1:6379/1'


class Production(Config):
    pass


config = {
    "Config": Config,
    "Development": Development,
    "Production": Production,
    "Default": Config,
}
