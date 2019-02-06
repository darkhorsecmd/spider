#! -*- encoding:utf-8 -*-

import requests

# 要访问的目标页面
targetUrl = "http://www.baidu.com"
# targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H24P351E4Q74R57D"
proxyPass = "BE0DBA04753B272A"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}
for i in range(5):
    print(proxies)
    resp = requests.get(targetUrl,proxies=proxies)

print(resp.status_code)
print(resp.text)
