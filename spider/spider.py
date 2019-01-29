from xmlUnit import ReadXML
from csvUnit import startReadCSV
from urllib import parse
from urllib import request
from lxml import etree
from gooseeker import GsExtractor
import os


if __name__ == '__main__':
    #配置文件路径
    configFileName = os.path.abspath(os.path.dirname(__file__))+"\\xmlUnit\\config.xml"
    csvFilePath = os.path.dirname(__file__) + "/csvUnit"

    #xml 和csv 实例化
    readxml = ReadXML.ReadXml(configFileName)
    readcsv = startReadCSV.startReadCSV(csvFilePath)

    #csv 开始读，对象可返回 tuple（key） 和 dict
    readcsv.startReadUrlList()

    #########################################以上为必须要执行的预备动作

    print(readcsv.getdic())  #dict
    print(readcsv.getKeyFileName())  ## key
    # for key in readcsv.getKeyFileName():
    #     listlinks = readcsv.getdic(key)
    #     for index in range(len(listlinks)):
    #         #每一个link 可能需要组装一下url
    #         oldLink = listlinks[index]
    #         link = parse.urljoin(key,oldLink)
    #