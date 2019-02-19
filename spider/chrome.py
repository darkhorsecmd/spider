from selenium import webdriver
from xmlUnit.ReadXML import ReadXml
import string
import zipfile
import os
import time


class chromes():
    def __init__(self):
        # 读取配置文件
        self.configPath = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\config.xml"
        self.readxml = ReadXml(self.configPath)
        # 代理服务器
        proxy_host = self.readxml.get_ItemValue("proxyHost")
        proxy_port = self.readxml.get_ItemValue("proxyPort")
        # 代理隧道验证信息
        proxy_username = self.readxml.get_ItemValue("proxyUser")
        proxy_password = self.readxml.get_ItemValue("proxyPass")
        scheme = 'http'
        plugin_path = None
        # 创建一个代理chrome插件
        if plugin_path is None:
            plugin_path = os.getcwd() + r'/{}_{}@http-dyn.abuyun.com_9020.zip'.format(proxy_username, proxy_password)

        manifest_json = """
           {
               "version": "1.0.0",
               "manifest_version": 2,
               "name": "Abuyun Proxy",
               "permissions": [
                   "proxy",
                   "tabs",
                   "unlimitedStorage",
                   "storage",
                   "<all_urls>",
                   "webRequest",
                   "webRequestBlocking"
               ],
               "background": {
                   "scripts": ["background.js"]
               },
               "minimum_chrome_version":"22.0.0"
           }
           """

        background_js = string.Template(
            """
            var config = {
                mode: "fixed_servers",
                rules: {
                    singleProxy: {
                        scheme: "${scheme}",
                        host: "${host}",
                        port: parseInt(${port})
                    },
                    bypassList: ["foobar.com"]
                }
              };

            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "${username}",
                        password: "${password}"
                    }
                };
            }

            chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
            );
            """
        ).substitute(
            host=proxy_host,
            port=proxy_port,
            username=proxy_username,
            password=proxy_password,
            scheme=scheme,
        )

        with zipfile.ZipFile(plugin_path, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        # 初始化chrome浏览器
        self.option = webdriver.ChromeOptions()
        self.option.add_extension(plugin_path)

        self.chromdriver_path = os.path.abspath(os.path.dirname(__file__)) + "\\chromedriver.exe"
        self.driver = webdriver.Chrome(options=self.option, executable_path=self.chromdriver_path)

    def get_html(self, url):
        self.driver.get(url)
        # print(self.driver.page_source)
        return self.driver.page_source

    def quit(self):
        self.driver.quit()

#
# if __name__ == '__main__':
#     chrome = chromes()
#     url = "https://www.baidu.com"
#     # 经过测试，每一个ip 都不一样
#     print(type(chrome.get_html(url=url)))
#     time.sleep(10)
#     print(chrome.get_html(url=url))
#     time.sleep(20)
#     print(chrome.get_html(url=url))
#     time.sleep(30)
#     print(chrome.get_html(url=url))
#     time.sleep(40)
#     print(chrome.get_html(url=url))
#     time.sleep(50)
#     print(chrome.get_html(url=url))
#     time.sleep(60)
#     print(chrome.get_html(url=url))
#     chrome.quit()
