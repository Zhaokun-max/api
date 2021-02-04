from test_partal_data.ProjectName import Project_Name
import json


class Publish_Data():
    '''发布建筑物'''
    @property
    def data_001(self):
        Name = Project_Name().str_Name
        #Name = Name.str_Name()
        data = {'address': "",
                'assetsInfo': '[{"massifName":"家住无","area":"100.00","price":"10000.00","certificateNo":"","originalContractor":"","address":"000","serialNumber":"00000000","bidStructure":"000000000","originalPurpose":"用提","attachmentRemark":"撒大声地"}]',
                'bondRatio': '10',
                'circulationType': "",
                'circulationTypeCode': "",
                'city': "2203",
                'commonOwnershipDesc': "",
                'county': "220322",
                'creditCode': "",
                'deliveryPeriod': "10",
                'endTime': "2021-01-29",
                'everyYearSumPrice': "10000.00",
                'forestOwner': "",
                'forestUser': "",
                'installmentDesc': "",
                'isSublet': False,
                'landCategory': "",
                'leaseDeposit': "10",
                'managementSubject': "",
                'managementSubjectCode': "1",
                'payDay': "100",
                'payType': "1",
                'projectName': "四平市梨树县蔡家镇蔡家村{}".format(Name),
                'projectNameInit': "嗷嗷啊所多",
                'projectSubType': "1",
                'projectType': "6",
                'province': "22",
                'startTime': "2021-01-18",
                'sumArea': "100.00",
                'sumMargin': 10000,
                'township': "220322106",
                'tradeType': "1",
                'transferType': "1",
                'transfereeIdCard': "",
                'transfereeName': "",
                'transfereePhoneNo': "",
                'transfereeType': "1",
                'village': "220322106201"}
        return data

    @property
    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()
    #第二步
    @property
    def data_002(self):
        json = {'assignmentCondition': '啊撒大声地',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json
    #第三步
    @property
    def data_003(self):
        data={'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data
    #获取图片地址
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()

    # @property
    # def data_004(self):
    #     ID = Publish_Data().read_01
    #     L= Publish_Data().read_photo()
    #     List=L
    #     json = {"projectId": ID,
    #             "files": [{"imgEnumType": 1, "urls": ["{}".format(List[1])]},
    #                       {"imgEnumType": 2, "urls": ["{}".format(List[2])]},
    #                       {"imgEnumType": 3, "urls": ["{}".format(List[3])]},
    #                       {"imgEnumType": 4, "urls": ["{}".format(List[4])]},
    #                       {"imgEnumType": 5, "urls": ["{}".format(List[5])]},
    #                       {"imgEnumType": 6, "urls": ["{}".format(List[6])]},
    #                       {"imgEnumType": 7, "urls": ["{}".format(List[7])]},
    #                       {"imgEnumType": 8, "urls": ["{}".format(List[8])]},
    #                       {"imgEnumType": 9, "urls": ["{}".format(List[9])]}]}
    #     return json
    #
    @property
    def data_005(self):
        '''确认承诺函'''
        ID=Publish_Data().read_01
        data={'projectId': "{}".format(ID), 'promiseHit': "", 'promiseHitOther': "萨达萨达萨达是"}
        return data

    @property
    def building_file(self):
        file = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        return file

class Publish_Cml():
    '''集体机动地'''
    @property
    def building_001(self):
        Name = Project_Name().str_Name
        data = {"projectType":"1",
                "tradeType":"1",
                "projectSubType":"1",
                "transfereeName":"",
                "transfereeIdCard":"",
                "transfereePhoneNo":"",
                "creditCode":"",
                "transfereeType":"1",
                "city":"2203",
                "county":"220322",
                "township":"220322106",
                "village":"220322106208",
                "projectName":"四平市梨树县蔡家镇下坎子村这是标的名称{}".format(Name),
                "projectNameInit":"{}".format(Name),
                "address":"这是详细地址",
                "managementSubject":"",
                "managementSubjectCode":"2",
                "landCategory":"",
                "commonOwnershipDesc":"",
                "forestOwner":"",
                "forestUser":"",
                "province":"22",
                "sumArea":"100.00",
                "sumPrice":"10000.00",
                "transferType":"1",
                "payType":"1",
                "payDay":"200",
                "startTime":"2021-01-01",
                "endTime":"2021-04-30",
                "circulationType":"",
                "circulationTypeCode":"",
                "bondRatio":"10",
                "deliveryPeriod":"",
                "leaseDeposit":"",
                "installmentDesc":"",
                "sumMargin":1000,
                "assetsInfo":"[{\"massifName\":\"这是第一个地块\",\"area\":\"100.00\",\"type\":\"1\",\"price\":\"10000.00\",\"toEast\":\"东田大戈壁\",\"toWest\":\"女儿国\",\"toSouth\":\"南田沙漠\",\"toNorth\":\"俄罗斯\",\"lastYearCrop\":\"大豆，小米\",\"yearBeforeLastCrop\":\"小米，高粱\",\"attachment\":\"大豆苷\",\"originalContractor\":\"无承包人\",\"certificateNo\":\"852041963852852\"}]"}
        return data

    @property
    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()

    # 第二步
    @property
    def building_002(self):
        json = {'assignmentCondition': '这是一个资格条件',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json

    # 第三步
    @property
    def building_003(self):
        data = {'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data

    # 获取图片地址
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()

    # @property
    # def building_004(self):
    #     ID = self.read_01
    #     L = self.read_photo()
    #     List = L
    #     data=json.dumps({'projectId':eval(ID),
    #              'files':[{'imgEnumType':1,'urls':'{0}'.format(List[0]).strip()},
    #                       {'imgEnumType':2,'urls':'{0}'.format(List[1]).strip()},
    #                       {'imgEnumType':3,'urls':'{0}'.format(List[2]).strip()},
    #                       {'imgEnumType':4,'urls':'{0}'.format(List[3]).strip()},
    #                       {'imgEnumType':5,'urls':'{0}'.format(List[4]).strip()},
    #                       {'imgEnumType':6,'urls':'{0}'.format(List[5]).strip()},
    #                       {'imgEnumType':7,'urls':'{0}'.format(List[6]).strip()},
    #                       {'imgEnumType':8,'urls':'{0}'.format(List[7]).strip()},
    #                       {'imgEnumType':9,'urls':'{0}'.format(List[8]).strip()}]})
    #     return data

    @property
    def building_005(self):
        '''重大事项提示'''
        ID = self.read_01
        data = {'projectId': "{}".format(ID), 'promiseHit': "这是涉及标的各种补贴的约定", 'promiseHitOther': "这是添加的其他提示"}
        return data

    @property
    def building_file(self):
        file = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        return file

class Publish_Clf():
    '''农户承包地'''
    @property
    def clf_001(self):
        Name = Project_Name().str_Name
        data = {"projectType":"1",
                "tradeType":"1",
                "projectSubType":"2",
                "transfereeName":"",
                "transfereeIdCard":"",
                "transfereePhoneNo":"",
                "creditCode":"",
                "transfereeType":"1",
                "city":"2203",
                "county":"220322",
                "township":"220322106",
                "village":"220322106202",
                "projectName":"四平市梨树县蔡家镇横道子村{}".format(Name),
                "projectNameInit":"表弟内容",
                "address":"这还是个详细地址",
                "managementSubject":"",
                "managementSubjectCode":"3",
                "landCategory":"1",
                "commonOwnershipDesc":"这是共有权人",
                "forestOwner":"",
                "forestUser":"",
                "province":"22",
                "sumArea":"100.00",
                "sumPrice":"10000.00",
                "transferType":"1",
                "payType":"1",
                "payDay":"100",
                "startTime":"2021-01-04","endTime":"2021-02-28",
                "circulationType":"","circulationTypeCode":"",
                "bondRatio":"10","deliveryPeriod":"","leaseDeposit":"",
                "installmentDesc":"","sumMargin":1000,
                "assetsInfo":"[{\"massifName\":\"这是一个地块\",\"area\":\"100.00\",\"type\":\"1\",\"price\":\"10000.00\",\"toEast\":\"日本\",\"toWest\":\"尼泊尔\",\"toSouth\":\"越南\",\"toNorth\":\"蒙古\",\"lastYearCrop\":\"痘痘\",\"yearBeforeLastCrop\":\"土豆土豆\",\"attachment\":\"高粱\",\"originalContractor\":\"\",\"certificateNo\":\"\"}]"}
        return data

    @property
    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()

    # 第二步
    @property
    def clf_002(self):
        json = {'assignmentCondition': '这是一个资格条件',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json

    # 第三步
    @property
    def clf_003(self):
        data = {'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data

    # 获取图片地址
    @property
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()

    @property
    def clf_004(self):
        ID = self.read_01
        L = self.read_photo
        List = L
        json = {"projectId":ID,
                 "files":[{"imgEnumType":1,"urls":["{}".format(List[1])]},
                          {"imgEnumType":2,"urls":["{}".format(List[2])]},
                          {"imgEnumType":3,"urls":["{}".format(List[3])]},
                          {"imgEnumType":4,"urls":["{}".format(List[4])]},
                          {"imgEnumType":5,"urls":["{}".format(List[5])]},
                          {"imgEnumType":6,"urls":["{}".format(List[6])]},
                          {"imgEnumType":7,"urls":["{}".format(List[7])]},
                          {"imgEnumType":8,"urls":["{}".format(List[8])]},
                          {"imgEnumType":9,"urls":["{}".format(List[9])]}]}

        return json

    @property
    def clf_005(self):
        '''重大事项提示'''
        ID = self.read_01
        data = {'projectId': "{}".format(ID), 'promiseHit': "这是涉及标的各种补贴的约定", 'promiseHitOther': "这是添加的其他提示"}
        return data

    @property
    def building_file(self):
        file = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        return file

class Publish_Woodland():
    '''林地林木'''
    @property
    def building_001(self):
        Name = Project_Name().str_Name
        data = {"projectType":"2",
                "tradeType":"1",
                "projectSubType":"1","transfereeName":"","transfereeIdCard":"",
                "transfereePhoneNo":"","creditCode":"","transfereeType":"1","city":"2203",
                "county":"220322","township":"220322106","village":"220322106203",
                "projectName":"四平市梨树县蔡家镇敬友村{}".format(Name),
                "projectNameInit":"name","address":"这是详细地址",
                "managementSubject":"","managementSubjectCode":"1","landCategory":"",
                "commonOwnershipDesc":"","forestOwner":"这是林木的所有权人啊","forestUser":"这是那个人",
                "province":"22","sumArea":"100.00","sumPrice":"10000.00","sumTreeNumber":1000,
                "transferType":"1","payType":"1","payDay":"100","startTime":"2021-01-03",
                "endTime":"2021-02-23","circulationType":"","circulationTypeCode":"",
                "bondRatio":"10","deliveryPeriod":"10","isSublet":None,"leaseDeposit":"",
                "installmentDesc":"","sumMargin":1000,"assetsInfo":"[{\"massifName\":\"第一块林地\",\"area\":\"100.00\",\"price\":\"10000.00\",\"toEast\":\"澳大利亚\",\"toWest\":\"非洲\",\"toSouth\":\"南极\",\"toNorth\":\"北极圈\",\"woodClass\":\"这是林版\",\"smallClass\":\"这是小班啊\",\"attachment\":\"啥也没有啊附着物\",\"originalContractor\":\"\",\"certificateNo\":\"\",\"serialNumber\":\"12345678923456\",\"forestSpecies\":\"萨达萨达多\",\"forestList\":[{\"treeSpecies\":\"这是树种\",\"treeNumber\":\"1000\"},{\"treeSpecies\":\"\",\"treeNumber\":\"\"},{\"treeSpecies\":\"\",\"treeNumber\":\"\"}]}]","projectId":"544"}
        return data

    @property
    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()

    # 第二步
    @property
    def building_002(self):
        json = {'assignmentCondition': '这是一个资格条件',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json

    # 第三步
    @property
    def building_003(self):
        data = {'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data

    # 获取图片地址
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()

    # @property
    # def building_004(self):
    #     ID = self.read_01
    #     L = self.read_photo()
    #     List = L
    #     json ={"projectId":ID,
    #              "files":[{"imgEnumType":1,"urls":["{}".format(List[1])]},
    #                       {"imgEnumType":2,"urls":["{}".format(List[2])]},
    #                       {"imgEnumType":3,"urls":["{}".format(List[3])]},
    #                       {"imgEnumType":4,"urls":["{}".format(List[4])]},
    #                       {"imgEnumType":5,"urls":["{}".format(List[5])]},
    #                       {"imgEnumType":6,"urls":["{}".format(List[6])]},
    #                       {"imgEnumType":7,"urls":["{}".format(List[7])]},
    #                       {"imgEnumType":8,"urls":["{}".format(List[8])]},
    #                       {"imgEnumType":9,"urls":["{}".format(List[9])]}]}
    #     return json

    @property
    def building_005(self):
        '''重大事项提示'''
        ID = self.read_01
        data = {'projectId': "{}".format(ID), 'promiseHit': "这是涉及标的各种补贴的约定", 'promiseHitOther': "这是添加的其他提示"}
        return data

    @property
    def building_file(self):
        file = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        return file

class Publish_water:
    '''水面'''
    @property
    def building_001(self):
        Name = Project_Name().str_Name
        data = {"projectType":"3","tradeType":"1","projectSubType":"1","transfereeName":"",
                "transfereeIdCard":"","transfereePhoneNo":"","creditCode":"",
                "transfereeType":"1","city":"2203","county":"220322","township":"220322106",
                "village":"220322106203","projectName":"四平市梨树县蔡家镇敬友村{}".format(Name),
                "projectNameInit":"name","address":"这是详细地址","managementSubject":"",
                "managementSubjectCode":"1","landCategory":"","commonOwnershipDesc":"",
                "forestOwner":"","forestUser":"","province":"22","sumArea":"100.00",
                "sumPrice":"100000.00","transferType":"1","payType":"1","payDay":"100",
                "startTime":"2021-01-01","endTime":"2021-02-28","circulationType":"",
                "circulationTypeCode":"","bondRatio":"10","deliveryPeriod":"10",
                "isSublet":None,"leaseDeposit":"","installmentDesc":"","sumMargin":10000,
                "assetsInfo":"[{\"massifName\":\"这是水面名称\",\"area\":\"100.00\",\"price\":\"100000.00\",\"toEast\":\"内蒙个\",\"toWest\":\"东土大唐\",\"toSouth\":\"老挝\",\"toNorth\":\"俄罗斯蒙古\",\"attachment\":\"没有附属设施\",\"certificateNo\":\"12345676432123\",\"originalPurpose\":\"原用途养鱼\",\"originalContractor\":\"没人啊\"}]","projectId":"544"}
        return data

    @property
    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()

    # 第二步
    @property
    def building_002(self):
        json = {'assignmentCondition': '这是一个资格条件',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json

    # 第三步
    @property
    def building_003(self):
        data = {'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data

    # 获取图片地址
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()

    # @property
    # def building_004(self):
    #     ID = self.read_01
    #     L = self.read_photo()
    #     List = L
    #     json = {"projectId":ID,
    #              "files":[{"imgEnumType":1,"urls":["{}".format(List[1])]},
    #                       {"imgEnumType":2,"urls":["{}".format(List[2])]},
    #                       {"imgEnumType":3,"urls":["{}".format(List[3])]},
    #                       {"imgEnumType":4,"urls":["{}".format(List[4])]},
    #                       {"imgEnumType":5,"urls":["{}".format(List[5])]},
    #                       {"imgEnumType":6,"urls":["{}".format(List[6])]},
    #                       {"imgEnumType":7,"urls":["{}".format(List[7])]},
    #                       {"imgEnumType":8,"urls":["{}".format(List[8])]}]}
    #     return json

    @property
    def building_005(self):
        '''重大事项提示'''
        ID = self.read_01
        data = {'projectId': "{}".format(ID), 'promiseHit': "这是涉及标的各种补贴的约定", 'promiseHitOther': "这是添加的其他提示"}
        return data

    @property
    def building_file(self):
        file = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        return file

class Publish_Equipment:
    '''设备'''
    @property
    def building_001(self):
        Name = Project_Name().str_Name
        data = {"projectType":"7","tradeType":"1","projectSubType":"1","transfereeName":"",
                "transfereeIdCard":"","transfereePhoneNo":"","creditCode":"",
                "transfereeType":"1","city":"2203","county":"220322",
                "township":"220322106","village":"220322106202",
                "projectName":"四平市梨树县蔡家镇横道子村{}".format(Name),"projectNameInit":"name","address":"",
                "managementSubject":"","managementSubjectCode":"1","landCategory":"",
                "commonOwnershipDesc":"","forestOwner":"","forestUser":"","province":"22",
                "sumPrice":"100000.00","sumArea":"1000.00","transferType":"1","payType":"1",
                "payDay":"100","startTime":"","endTime":"","circulationType":"","circulationTypeCode":"",
                "bondRatio":"10","deliveryPeriod":"","isSublet":None,"leaseDeposit":"",
                "installmentDesc":"","sumMargin":10000,
                "assetsInfo":"[{\"massifName\":\"这是设备名称\",\"manufactureBrand\":\"盼达厂家\",\"productModel\":\"12456A\",\"manufactureDate\":\"2022-01-12\",\"area\":\"1000.00\",\"price\":\"100000.00\",\"otherCondition\":\"小猪佩奇\",\"originalContractor\":\"全新的\",\"certificateNo\":\"8520258520\"}]","projectId":"544"}
        return data

    @property
    def read_01(self):
        with open('ID', 'r') as f:
            return f.read()

    # 第二步
    @property
    def building_002(self):
        json = {'assignmentCondition': '这是一个资格条件',
                'bidType': '1',
                'increaseAmount': '1000',
                'increaseTime': '60',
                'projectId': '{}'.format(self.read_01),
                'qualificationRestriction': '1',
                'unBidSel': '1'}
        return json

    # 第三步
    @property
    def building_003(self):
        data = {'bizType': '', 'width': '1024', 'height': '768', 'Content-Disposition': 'form-data'}
        return data

    # 获取图片地址
    def read_photo(self):
        with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
            return f.readlines()

    @property
    def building_004(self):
        ID = self.read_01
        L = self.read_photo()
        List = L
        json = {"projectId": ID,
                "files": [{"imgEnumType": 1, "urls": ["{}".format(List[1])]},
                          {"imgEnumType": 12, "urls": ["{}".format(List[2])]},
                          {"imgEnumType": 3, "urls": ["{}".format(List[3])]},
                          {"imgEnumType": 4, "urls": ["{}".format(List[4])]},
                          {"imgEnumType": 13, "urls": ["{}".format(List[5])]},
                          {"imgEnumType": 15, "urls": ["{}".format(List[6])]}]}
        return json

    @property
    def building_005(self):
        '''重大事项提示'''
        ID = self.read_01
        data = {'projectId': "{}".format(ID), 'promiseHit': "这是涉及标的各种补贴的约定", 'promiseHitOther': "这是添加的其他提示"}
        return data

    @property
    def building_file(self):
        file = {"file": ("123.jpg", open(r'C:\Users\Administrator\Desktop\123.jpg', 'rb'), "image/jpeg")}
        return file