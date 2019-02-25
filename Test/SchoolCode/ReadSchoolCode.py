import csv
import re


def zhengze(s):
    pattern = re.compile(r'[^\d]+(\d+)[^\d]+')
    res = re.findall(pattern, s)
    return res


csvfile = open("学校代码.csv", 'r', encoding='UTF-8')
reader = csv.reader(csvfile)
result = []
for item in reader:
    str = "".join(item[0].split())
    print(str)
    print(zhengze(str))


csvfile.close()
