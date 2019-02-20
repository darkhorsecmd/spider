import os

if __name__ == '__main__':
    print(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # E:\19年文件\毕设爬虫\spider\spider
    detail_path = path + "\\xmlUnit+\\linkList_detail"
    print(detail_path)
