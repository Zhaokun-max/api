import xml.dom.minidom

def getXml(values=None):
    '''获取单节点的数据内容'''
    #读取xml
    xmlFile=xml.dom.minidom.parse('data.xml')
    #进行documentElement解析
    db=xmlFile.documentElement
    #节点层次
    itemList=db.getElementsByTagName(values)
    #取到第一个数据
    item=itemList[0]
    #取到对应的 第一个数据
    return item.firstChild.data


def getUser(parent='PanDa',child=None):
    '''获取单节点的数据内容'''
    #读取xml
    xmlFile=xml.dom.minidom.parse('data.xml')
    #进行documentElement解析
    db=xmlFile.documentElement
    #节点层次
    itemList=db.getElementsByTagName(parent)
    #取到第一个数据
    item=itemList[0]
    #取到对应的 第一个数据
    return item.getAttribute(child)

print(getUser(child='age'))


