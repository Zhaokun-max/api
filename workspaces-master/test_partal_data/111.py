import re
import json
def read_photo():
    with open('../test_Portal/photo', 'r', encoding='utf-8') as f:
        return f.readlines()

        #return json.dumps(f.readlines())

def building_004():
    L = read_photo()
    List=L

#    print(List['allPath'])
    json = {"projectId": 1,
            "files": [{"imgEnumType": 1, "urls": "{}".format(List[0]).split()}]}
                      # {"imgEnumType": 2, "urls": ["{}".format(List[2])]},
                      # {"imgEnumType": 3, "urls": ["{}".format(List[3])]},
                      # {"imgEnumType": 4, "urls": ["{}".format(List[4])]},
                      # {"imgEnumType": 5, "urls": ["{}".format(List[5])]},
                      # {"imgEnumType": 6, "urls": ["{}".format(List[6])]},
                      # {"imgEnumType": 7, "urls": ["{}".format(List[7])]},
                      # {"imgEnumType": 8, "urls": ["{}".format(List[8])]}]}
    print(type(json))
    print(json)

#building_004()

data={'projectId': 1,
            'files': [{'imgEnumType': 1, 'urls': '{1111}'}]}
# s=json.dumps(data)
# print(s)
# print(type(s))
data1=str({"projectId": 12})
de=[]
data = str({"files": [{"imgEnumType": int(1), "urls": "213"},
                                  {"imgEnumType": int(2), "urls": "123"},
                                  {"imgEnumType": int(3), "urls": "123"},
                                  {"imgEnumType": int(4), "urls": "12312"}]})
print(data)
json.dumps()