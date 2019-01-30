from xmlUnit import ReadXML
from csvUnit import startReadCSV
from urllib import request
from lxml import etree
from gooseeker import GsExtractor
import os


def parse(url,key):
    linksParseRule = key  #教师list的url 的解析规则
    PageDetailRule = key+"_detail"  #每一个教师信息的解析规则
    # print(url)
    # print(linkParseRule)
    # print(PageDetailRule)

    pass


if __name__ == '__main__':
    # 配置文件路径
    configFileName = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\config.xml"
    csvFilePath = os.path.dirname(__file__) + "/csvUnit"

    # xml 和csv 实例化
    readxml = ReadXML.ReadXml(configFileName)
    readcsv = startReadCSV.startReadCSV(csvFilePath)

    # csv 开始读，对象可返回 tuple（key） 和 dict
    readcsv.startReadUrlList()

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
            parse(link,keyname)
