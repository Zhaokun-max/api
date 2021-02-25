import os

#当前目录
#print(os.path.dirname(__file__))
#上一级目录
#print(os.path.dirname(os.path.dirname(__file__)))
# base_url=os.path.dirname(os.path.dirname(__file__))
# print(os.path.join(base_url,'data','login.yaml'))

#文件的路径
def filePath(fileDir='data', fileName='login.yaml'):
    '''
    :param fileDir: 目录
    :param filename: 文件的名称
    :return:
    '''
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)), fileDir, fileName)
21212

