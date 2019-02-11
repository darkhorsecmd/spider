from xml.dom.minidom import parse
import xml.dom.minidom
import os



class ReadTreeXml:
    def __init__(self, rootPath):
        self.linkPath = rootPath
        self.linkNamePathList = os.listdir(self.linkPath)
        self.links = []
        self.__parseUrl()  # 对象创建的时候，就已经读取好所有的link的内容，准备以list方式返回

    def __myparse(self, file_path):  # 将每一个listurl 解析出所有的url并存入一个list总集合中
        DOMTree = xml.dom.minidom.parse(file_path)
        root = DOMTree.documentElement
        itemList = root.getElementsByTagName("item")
        for item in itemList:
            self.links.append(item.getElementsByTagName('link')[0].childNodes[0].data)

    def __parseUrl(self):  # 待解析每一个 listurl
        for eachlink in self.linkNamePathList:
            path_pre = self.linkPath + "\\" + eachlink
            self.__myparse(path_pre)

    def getUrlList(self):
        return self.links


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    read = ReadTreeXml(os.path.dirname(__file__))  # 注意在别的包里面调用的话， 这样写  ReadTreeXml.ReadTreeXml

    list = read.getUrlList()
    print(list)
    # file_name = os.path.abspath(os.path.dirname(__file__)) + "\\Temp\\" +"text.csv"
