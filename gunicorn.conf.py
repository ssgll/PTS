# -*- coding:utf-8 -*-
import os
import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

chdir = "/root/pts"
debug = True
loglevel = "info"
bind = "0.0.0.0:80"
pidfile = "logs/gunicorn.pid"
accesslog = "logs/access.log"
errorlog = "logs/error.log"
daemon = True
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
x_forwarded_for_header = "X-FORWARDED-FOR"
