import os
from xmlUnit.ReadDetailXML import ReadDetailXML
from tools.MoveFIle import MoveFile
from tools.Mylog import Mylog
from save import save
from tools.zhengze import zhengze

clear_log = Mylog("清洗数据日志")
zhengze = zhengze()
data_inserFun = save()

if __name__ == '__main__':
    # 详情文件夹路径
    detail_path = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "\\xmlUnit\\linkList_detail"
    # 获取详情文件夹所有文件名
    ListFiles = os.listdir(detail_path)
    # ListFiles  # ['东南大学_经济管理学院_detail9fda5dff-35cf-11e9-bd3a-acd1b8a68732.xml', '东南大学_经济管理学院_detail9ff5788d-35cf-11e9-a062-acd1b8a68732.xml']
    # detail_path # E:\19年文件\毕设爬虫\spider\spider\xmlUnit\linkList_detail

    # 预先定义一个处理xxxxdetail.xml文件的对象
    readDetail = ReadDetailXML()
    moveFile = MoveFile()
    mylog = Mylog("ReadDetail")

    # 这里需要加一个探测功能：探测 linkList_detail文件夹里面是否有文件
    # pass
    for index in range(len(ListFiles)):
        try:
            file_path = detail_path + "\\" + ListFiles[index]  # detail xml文件路径
            readDetail.setFilePath(file_path)  # 设置detail xml文件路径,并开始读文件
            Info_Dict = readDetail.get_DetailDict()
            if len(Info_Dict)!=0:
                #准备处理保存相关数据
                data_inserFun.insert_data(Info_Dict,readDetail.gettable_dict())
            else:
                # Info_Dict 为空，没想好要干啥，先空着
                pass

            moveFile.move_EachFileFromlinkList_detail_To_Last(
                file_path,detail_path+"_Last")  # 解析好每一个文件则需要将这个文件移动到 linkList_detail_Last 文件夹里面
        except Exception as e:
            mylog.error(str(e))
