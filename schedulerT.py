from flask import Flask, request
from flask_apscheduler import APScheduler


class Config(object):  # 创建配置，用类
    # 任务列表
    JOBS = [
        # {  # 第一个任务
        #     'id': 'job1',
        #     'func': '__main__:job_1',
        #     'args': (1, 2),
        #     'trigger': 'cron', # cron表示定时任务
        #     'hour': 19,
        #     'minute': 27
        # },
        {  # 第二个任务，每隔5S执行一次
            "id": "job2",
            "func": "__main__:method_test",  # 方法名
            "args": (1, 2),  # 入参
            "trigger": "interval",  # interval表示循环任务
            "seconds": 5,
        }
    ]


def method_test(a, b):
    print(1)


app = Flask(__name__)
app.config.from_object(Config())  # 为实例化的flask引入配置


##
@app.route("/hello", methods=["POST", "GET"])
def check():
    return "success", 200


if __name__ == "__main__":
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run()
