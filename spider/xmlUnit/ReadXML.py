from xml.dom.minidom import parse
import xml.dom.minidom

# DOMTree = xml.dom.minidom.parse("config.xml")
# start = DOMTree.documentElement
# print("root element:%s" % start.getAttribute("appkey"))
# db_host = start.getElementsByTagName('db_host')[0]
# print(db_host.childNodes[0].data)
#

class ReadXml:
    '''
        此类只适用于只有二层结构的xml
        构造函数需要传入 xml文件名
        get_RootAttribute 需要传入 属性名
        get_ItemValue 需要传入 标签名
    '''
    def __init__(self, FileName):
        self.DOMTree = xml.dom.minidom.parse(FileName)
        self.root = self.DOMTree.documentElement

    def get_RootAttribute(self, attribute):
        return self.root.getAttribute(attribute)

    def get_ItemValue(self, ValueTag):
        return self.root.getElementsByTagName(ValueTag)[0].childNodes[0].data

    pass
if __name__ == '__main__':
    readxml = ReadXml("config.xml")
    print(readxml.get_RootAttribute("appkey"))
    print(readxml.get_ItemValue("db_tablename"))
    print(readxml.get_ItemValue("db_name"))