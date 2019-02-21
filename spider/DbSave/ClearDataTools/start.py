import os

def parseFile(file_path):
    pass

if __name__ == '__main__':
    #详情文件夹路径
    detail_path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))+"\\xmlUnit\\linkList_detail"
    #获取详情文件夹所有文件名
    ListFiles = os.listdir(detail_path)

    print(ListFiles)#['东南大学_经济管理学院_detail9fda5dff-35cf-11e9-bd3a-acd1b8a68732.xml', '东南大学_经济管理学院_detail9ff5788d-35cf-11e9-a062-acd1b8a68732.xml']
    print(detail_path) #E:\19年文件\毕设爬虫\spider\spider\xmlUnit\linkList_detail

    for index in range(len(ListFiles)):
        file_path = detail_path+"\\"+ListFiles[index]
        parseFile(file_path)