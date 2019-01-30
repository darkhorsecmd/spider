
from xml.dom.minidom import parse
import xml.dom.minidom
import os

# linkPath = os.path.dirname(__file__) + "/Temp"
# linkNamePathList = os.listdir(linkPath)
# for linkName in linkNamePathList:
#     path_LinkName = linkPath + "/"+linkName


class ReadTreeXml:
    def __init__(self, rootPath):
        self.linkPath = rootPath + "/Temp"
        self.linkNamePathList = os.listdir(self.linkPath)
        self.links = []
        self.__parseUrl()  # 对象创建的时候，就已经读取好所有的link的内容，准备以list方式返回

    def __myparse(self, path):
        DOMTree = xml.dom.minidom.parse(path)
        root = DOMTree.documentElement
        itemList = root.getElementsByTagName("item")
        for item in itemList:
            self.links.append(item.getElementsByTagName('link')[0].childNodes[0].data)


    def __parseUrl(self):
        for eachlink in self.linkNamePathList:
            path_pre = self.linkPath + "/" + eachlink
            print(path_pre)
            self.__myparse(path_pre)

    def getUrlList(self):
        return self.links

if __name__ == '__main__':
    read = ReadTreeXml(os.path.dirname(__file__))  #注意在别的包里面调用的话， 这样写  ReadTreeXml.ReadTreeXml
    list = read.getUrlList()
    print(list)