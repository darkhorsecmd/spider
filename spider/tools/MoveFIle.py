import os
import shutil
from tools.Mylog import Mylog

#此方法不具备通用性，专门给爬虫 移动链接
class MoveFile():
    mylog = Mylog("MoveFile")

    def __init__(self):
        self.rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    def move_EachFileFromlinkList_detail_To_Last(self,detailFilePath):
        #每调用一次则将  detailFilePath 文件 移动到Last文件夹
        pass





    def move_linkListTo_Last(self, school_name, academy_name):
        xmlSrcPath = self.rootPath + "\\xmlUnit\\linkList"
        xmlDesPath = self.rootPath + "\\xmlUnit\\linkList_Last"
        xmldirs = os.listdir(xmlSrcPath)
        try:
            for file in xmldirs:
                shutil.move(xmlSrcPath + "\\" + file, xmlDesPath + "\\" + file)
            print("from linkList to linkList_Last with file" + school_name + "\\" + academy_name + "move ok!")
        except Exception as e:
            MoveFile.mylog.error(
                "from linkList to linkList_Last with file" + school_name + "\\" + academy_name + str(e))

    def move_csvlistTo_Last(self, school_name, academy_name):
        ReadOk_schoolAndacademy_namePath = "\\" + school_name + "\\" + academy_name + ".csv"
        Des_schoolPath = "\\" + school_name + "\\"
        csvSrcPath = self.rootPath + "\\csvUnit\\csvlist" + ReadOk_schoolAndacademy_namePath  # 已经读好的csv文件的路径
        csvDesPath = self.rootPath + "\\csvUnit\\csvlist_Last" + Des_schoolPath  # 移动到这个位置文件夹
        csvDesFilePath = self.rootPath + "\\csvUnit\\csvlist_Last" + ReadOk_schoolAndacademy_namePath  # 真正移动到的位置
        try:
            if not os.path.exists(csvDesPath):  #如果目标文件夹不存在，则创建文件夹
                os.makedirs(csvDesPath)
            shutil.move(csvSrcPath, csvDesFilePath)
            # csvdirs = os.listdir(csvSrcPath)
            # for file in csvdirs:
            #     shutil.move(csvSrcPath+"\\"+file,csvDesPath+"\\"+file)
            print("move csvlist from " + csvSrcPath + " to " + csvDesFilePath)
        except Exception as e1:
            MoveFile.mylog.error("move csvlist from " + csvSrcPath + " to " + csvDesFilePath + " EXCEPT:" + str(e1))


if __name__ == '__main__':
    # 下面是一些使用样例
    mov = MoveFile()
    mov.move_csvlistTo_Last("东南大学", "机械工程学院2")
