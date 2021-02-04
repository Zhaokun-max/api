import csv

#读取csv按照列表方式读取，按照字典方式读取

def readCsvList():
    with open('csv.csv','r') as f:
        reader=csv.reader(f)
        #不想读去title加next，读取的话去掉
        next(reader)
        for item in reader:
            print(item[0])
            #如果读取的不是list类型可以强制转换
            #print(list(item)[0])
readCsvList()

#按照字典方式读取

def readCsvDict():
    with open('csv.csv','r') as f:
        #字典方式读取循环
        #自恋必须读取title
        reader=csv.DictReader(f)
        for item in reader:
            #print(dict(item))
            print(dict(item)['测试地址'])

