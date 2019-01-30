from xmlUnit import ReadXML
from xmlUnit import ReadTreeXML
from csvUnit import startReadCSV
from urllib import request
from lxml import etree
from gooseeker import GsExtractor
import os
import uuid
APPKEY=""

def GetlinkList(url,key):#url 可以作为前缀拼凑成完整的网页链接
    linksParseRule = key  # 教师list的url 的解析规则
    PageDetailRule = key + "_detail"  # 每一个教师信息的解析规则
    # 访问并读取网页内容
    conn = request.urlopen(url)
    doc = etree.HTML(conn.read())

    extra = GsExtractor()  # 生成xsltExtractor对象
    extra.setXsltFromAPI(APIKey=APPKEY, theme=linksParseRule)  # 获取规则文件，并读取
    xpathCss_selector_Xml_Content = extra.getXslt()  # 截取的xpath的xml规则文件
    # Unicode_PageResult = extra.extract(doc)  # 获取教师页所有链接
    # pageResult = Unicode_PageResult.encode('utf-8')
    pageResult=extra.extract(doc)  # 获取教师页所有链接
    # 暂时写入文件，查看一下
    id = uuid.uuid1()
    file_name = os.path.abspath(os.path.dirname(__file__)) + "\\Temp\\" + str(uuid.uuid1()) + ".xml"
    open(file_name, "wb").write(pageResult)


def parseDetail(url, rule):
    pass


def parse(url, key):
    GetlinkList(url,key)



if __name__ == '__main__':
    # 配置文件路径
    configFileName = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\config.xml"
    csvFilePath = os.path.dirname(__file__) + "/csvUnit"

    # xml 和csv 实例化
    readxml = ReadXML.ReadXml(configFileName)
    readcsv = startReadCSV.startReadCSV(csvFilePath)

    # csv 开始读，对象可返回 tuple（key） 和 dict
    readcsv.startReadUrlList()

    #给全局变量APPKEY 赋值
    APPKEY = readxml.get_RootAttribute("appkey")

    #########################################以上为必须要执行的预备动作
    #
    # print(readcsv.getdic())  #dict
    # print(readcsv.getKeyFileName())  ## key
    for fileNameIndex in range(len(readcsv.getKeyFileName())):
        keyname = readcsv.getKeyFileName()[fileNameIndex]
        listlinks = readcsv.getdic()[keyname]
        for linkIndex in range(len(listlinks)):
            # 每一个link 后面将作为平凑的前缀
            link = listlinks[linkIndex][0]
            parse(link, keyname)
