# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from RandomUserAgent import RandomUserAgent
from urllib import parse

def getallurl(url=r'http://www.civil.tsinghua.edu.cn/ce/83.html'):
    rd = RandomUserAgent()
    headers = {"User-Agent": rd.get_RanDomAgent()}
    r = requests.get(url=url,headers=headers)
    s = BeautifulSoup(r.content, 'lxml')

    atag = s.find_all('a')
    listurl = []
    for each in atag:
        try:
            listurl.append([each['href'], each.text])
        except:
            listurl.append(['', each.text])
    return listurl


if __name__ == '__main__':
    # inputurl=str(input("input the url: \n"))
    # listurl=getallurl(inputurl)
    listurl = getallurl()
    for i in range(len(listurl)):
        myurl = parse.urljoin('http://www.civil.tsinghua.edu.cn/ce/83.html',listurl[i][0])
        print("The %sth url is: %s, and the title is: %s \n" % (i, myurl, listurl[i][1]))
