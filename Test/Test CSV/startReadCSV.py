import os
import csv


class startReadCSV:
    def __init__(self):
        self.path = os.path.dirname(__file__) + "/csvlist"  # E:/19年文件/毕设爬虫/code/Test/Test CSV/csvlist
        self.ListFiles = os.listdir(self.path)  # 直接获取csvlist文件夹下的所有文件夹  ['nju.edu.cn',......]
        self.file_namelist=[] #保存所有的文件名 返回
        self.links = []  # 获取的每一个文件内的所有链接,为后面的存储方便点
        self.dic = {}  # key文件名 ，value为一个所有链接list

    def startReadUrlList(self):
        for index in range(len(self.ListFiles)): #每一个文件夹
            dir = self.path + "/" + self.ListFiles[index]  # E:/19年文件/毕设爬虫/code/Test/Test CSV/csvlist/nju.edu.cn
            files = os.listdir(dir)  # 依次进入每一个文件夹目录
            for f_index in range(len(files)): #每一个文件夹下的文件
                file_name = (os.path.splitext(files[f_index])[0])#获取单个文件名
                self.file_namelist.append(file_name)  #文件名存储到list中
                links = []  # 初始化
                filePath_name = dir + "/" + files[
                    f_index]  # 文件路径包括文件后缀   E:/19年文件/毕设爬虫/code/Test/Test CSV/csvlist/nju.edu.cn/im.nju.edu.cn.csv
                csvFile = open(filePath_name, "r")
                reader = csv.reader(csvFile)
                for line in reader: #文件内的每一行
                    links.append(line)
                    self.links.append(line)
                self.dic[file_name]=links  #院系名作为dic的key值，value是list 所有的链接
    def getKeyFileName(self):
        #返回 所有文件名tuple，因为这是作为key的
        return self.file_namelist

    def getdic(self):
        #返回最终的dic
        return self.dic


if __name__ == '__main__':
    #example
    reads = startReadCSV()
    reads.startReadUrlList()
    FileNameTuple = reads.getKeyFileName()
    print(FileNameTuple[0])
    dic = reads.getdic()
    print(dic[FileNameTuple[0]]) #{():[[],[]]}