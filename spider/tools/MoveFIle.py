import os
import shutil

class MoveFile():
    def __init__(self):
        self.rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    def move_linkListTo_Last(self):
        xmlSrcPath = self.rootPath + "\\xmlUnit\\linkList"
        xmlDesPath = self.rootPath + "\\xmlUnit\\linkList_Last"
        xmldirs = os.listdir(xmlSrcPath)
        for file in xmldirs:
            shutil.move(xmlSrcPath+"\\"+file,xmlDesPath+"\\"+file)
        print("from linkList to linkList_Last move ok!")

    def move_csvlistTo_Last(self):
        csvSrcPath = self.rootPath + "\\csvUnit\\csvlist"
        csvDesPath = self.rootPath + "\\csvUnit\\csvlist_Last"
        csvdirs = os.listdir(csvSrcPath)
        for file in csvdirs:
            shutil.move(csvSrcPath+"\\"+file,csvDesPath+"\\"+file)
        print("from csvlist to csvlist_Last move ok!")

if __name__ == '__main__':

    #下面是一些使用样例
    print(os.getcwd())
    print(os.path.dirname(__file__))
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    csvSrcPath = rootPath + "\\csvUnit\\csvlist"
    csvdirs = os.listdir(csvSrcPath)
    csvDesPath = rootPath + "\\csvUnit\\csvlist_Last"
    # for file in csvdirs:
    #     shutil.move(csvSrcPath + "\\" + file, csvDesPath + "\\" + file)
    # print(csvdirs)
    xmlSrcPath = rootPath + "\\xmlUnit\\linkList"
    xmldirs = os.listdir(xmlSrcPath)
    xmlDesPath = rootPath + "\\xmlUnit\\linkList_Last"
