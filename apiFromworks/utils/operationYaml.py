#对yaml文件进行操作
import yaml
from common.pubilc import filePath

class OperationYaml:
    def readYaml(self):
        #list列表
        with open(filePath(),'r',encoding='utf-8') as f:
            return list(yaml.safe_load_all(f))

    def dictYaml(self,fileDir='config',fileName='book.yaml'):
        #yaml.load 转换为字典格式
        with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
            return yaml.safe_load(f)

# if __name__ == '__main__':
#     obj=OperationYaml()
#     for item in obj.readYaml():
#         print(item)
# if __name__ == '__main__':
#     obj=OperationYaml()
#     print(obj.dictYaml()['book_002'])