import csv

def readCsv():
    data=list()
    with open('login.csv','r',encoding='utf-8') as f:
        #读取对象
        readr=csv.reader(f)
        #忽略title
        next(readr)
        for item in readr:
            data.append(item)
    return data

# for i in readCsv():
#     print(i)