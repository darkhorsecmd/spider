import os
import csv
import tools.mkdir


class startReadCSV:
    # 需要传入 当前所在位置的 rootpath
    def __init__(self, Getpath):
        self.path = Getpath + "/csvlist"  # E:/19年文件/毕设爬虫/code/Test/Test CSV/csvlist
        self.ListFiles = os.listdir(self.path)  # 直接获取csvlist文件夹下的所有文件夹  ['南京大学',......]
        self.file_namelist = []  # 保存所有的文件名 返回
        self.dic = {}  # key文件名 ，value为一个所有链接list

    def startReadUrlList(self):
        for index in range(len(self.ListFiles)):  # 每一个大学文件夹
            dir = self.path + "/" + self.ListFiles[index]  # E:/19年文件/毕设爬虫/code/Test/Test CSV/csvlist/南京大学
            files = os.listdir(dir)  # 获得 南京大学目录下的所有文件名，以list方式
            for f_index in range(len(files)):  # 每一个文件夹下的文件
                file_name = (os.path.splitext(files[f_index])[0])  # 获取学院名字
                self.file_namelist.append(self.ListFiles[index] + "_" + file_name)  # 格式："学校名_学院名"存储到list中，将来作为重要的key进行读取相关link
                links = []  # 初始化
                filePath_name = dir + "/" + files[
                    f_index]  # 文件路径包括文件后缀   E:/19年文件/毕设爬虫/code/Test/Test CSV/csvlist/南京大学/信息管理学院.csv
                csvFile = open(filePath_name, "r")
                reader = csv.reader(csvFile)
                for line in reader:  # 文件内的每一行
                    links.append(line)
                self.dic[self.ListFiles[index] + "_" + file_name] = links  # "学校名_学院名"作为dic的key值，value是list 所有的链接

    def getKeyFileName(self):
        # 返回 所有名tuple，因为这是作为key的
        return self.file_namelist

    def getdic(self):
        # 返回最终的dic 形式：
        #{
        # 1学校_学院:[[link1],[link2]]
        # 2学校_学院:[[link1],[link2]]
        #}
        return self.dic


if __name__ == '__main__':
    # example
    reads = startReadCSV(os.path.dirname(__file__))
    reads.startReadUrlList()
    FileNameTuple = reads.getKeyFileName()
    print(FileNameTuple[0])  #南京大学_信息管理学院
    dic = reads.getdic()
    print(dic[FileNameTuple[0]])  # {():[[],[]]} #csv文件里面的所有listurl链接
