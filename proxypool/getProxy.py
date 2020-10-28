# -*- coding: utf-8 -*-
from urllib import request
import re
from models import Pool, db


# 66ip
def ip_66():
    try:
        db.session.query(Pool).delete()
        db.session.commit()
    except Exception as e:
        pass
    tqsl = "100"
    url = "http://www.66ip.cn/mo.php?tqsl=" + tqsl
    html = request.urlopen(url).read().decode("gbk")
    pattern = "[\d+.]+\d:\d{0,}"
    ipList = re.findall(pattern, html)
    for ip in ipList:
        print(ip)


# 检查代理是否有效
def proxy_status(ip):
    user_agent = {
        "user-agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/86.0.4240.75 "
            "Safari/537.36 Edg/86.0.622.38 "
        )
    }
    test_url = "https://www.baidu.com/"
    proxie = {"http": ip}
    handler = request.ProxyHandler(proxie)
    openner = request.build_opener(handler)
    try:
        response = request.Request(test_url, headers=user_agent)
        html = openner.open(response, timeout=5)
        status = html.status
    except:
        status = 0
    return status


ip_66()
