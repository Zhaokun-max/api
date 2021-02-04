# import json
#
# #  转换为字典
#
# dict1=\
#     {
#     "info": {
#         "_postman_id": "40e6fa66-bb62-4cf3-82ed-96cd28142bfa",
#         "name": "rongxin",
#         "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
#     },
#     "item": [
#         {
#             "name": "断言",
#             "event": [
#                 {
#                     "listen": "test",
#                     "script": {
#                         "id": "f8e5463f-9ad3-426f-a3a8-1e9341483977",
#                         "exec": [
#                             "var jsonDate=JSON.parse(responseBody)\r",
#                             "\r",
#                             "pm.test(\"Status code is 200\", function () {\r",
#                             "    pm.response.to.have.status(200);\r",
#                             "});\r",
#                             "\r",
#                             "tests['第一位省事长春']=jsonDate.data[0].areaName=='长春市'\r",
#                             "\r",
#                             "tests['第二个省是吉林市']=jsonDate.data[1].areaName=='吉林'"
#                         ],
#                         "type": "text/javascript"
#                     }
#                 }
#             ],
#             "request": {
#                 "method": "GET",
#                 "header": [
#                     {
#                         "key": "Content-Type",
#                         "value": "application/json",
#                         "type": "text"
#                     }
#                 ],
#                 "url": {
#                     "raw": "http://api/api/v1.0/chanquan/area/selectAreaList/22/2",
#                     "host": [
#                         "http://api/"
#                     ],
#                     "path": [
#                         "api",
#                         "v1.0",
#                         "chanquan",
#                         "area",
#                         "selectAreaList",
#                         "22",
#                         "2"
#                     ]
#                 }
#             },
#             "response": []
#         },
#         {
#             "name": "获取code",
#             "event": [
#                 {
#                     "listen": "test",
#                     "script": {
#                         "id": "f8e5463f-9ad3-426f-a3a8-1e9341483977",
#                         "exec": [
#                             "var jsonData=JSON.parse(responseBody)\r",
#                             "\r",
#                             "//增加断言\r",
#                             "tests['验证code的名称']=jsonData.data[0].areaName==='长春市'\r",
#                             "\r",
#                             "\r",
#                             "postman.setEnvironmentVariable('areaCode',jsonData.data[1].areaCode)\r",
#                             ""
#                         ],
#                         "type": "text/javascript"
#                     }
#                 }
#             ],
#             "request": {
#                 "method": "POST",
#                 "header": [
#                     {
#                         "key": "Content-Type",
#                         "type": "text",
#                         "value": "application/json"
#                     }
#                 ],
#                 "url": {
#                     "raw": "http://test.portal.jlncjy.cacfintech.com/",
#                     "host": [
#                         "http://api/"
#                     ],
#                     "path": [
#                         "api",
#                         "v1.0",
#                         "chanquan",
#                         "area",
#                         "selectAreaList",
#                         "22",
#                         "2"
#                     ]
#                 }
#             },
#             "response": []
#         },
#         {
#             "name": "查看code",
#             "event": [
#                 {
#                     "listen": "test",
#                     "script": {
#                         "id": "f8e5463f-9ad3-426f-a3a8-1e9341483977",
#                         "exec": [
#                             "var jsonData=JSON.parse(responseBody)\r",
#                             "\r",
#                             "//增加断言\r",
#                             "tests['验证code的名称']=jsonData.data[0].areaCode==='2201'\r",
#                             "\r",
#                             "\r",
#                             "postman.setEnvironmentVariable('areaCode',jsonData.data[0].data.areaCode)\r",
#                             ""
#                         ],
#                         "type": "text/javascript"
#                     }
#                 }
#             ],
#             "request": {
#                 "method": "GET",
#                 "header": [
#                     {
#                         "key": "Content-Type",
#                         "type": "text",
#                         "value": "application/json"
#                     }
#                 ],
#                 "url": {
#                     "raw": "http://api//api/v1.0/chanquan/area/selectAreaList/22/{{areaCode}}",
#                     "host": [
#                         "http://api/"
#                     ],
#                     "path": [
#                         "api",
#                         "v1.0",
#                         "chanquan",
#                         "area",
#                         "selectAreaList",
#                         "22",
#                         "{{areaCode}}"
#                     ]
#                 }
#             },
#             "response": []
#         },
#         {
#             "name": "认证",
#             "event": [
#                 {
#                     "listen": "test",
#                     "script": {
#                         "id": "f8e5463f-9ad3-426f-a3a8-1e9341483977",
#                         "exec": [
#                             ""
#                         ],
#                         "type": "text/javascript"
#                     }
#                 }
#             ],
#             "request": {
#                 "method": "POST",
#                 "header": [
#                     {
#                         "key": "Content-Type",
#                         "value": "application/json",
#                         "type": "text"
#                     },
#                     {
#                         "key": "Cookie",
#                         "value": "PHPSESSID=test.rongxin.chanquan.por.jilin.sid=s%3Atest.rongxin.chanquan.por.jilin.sid%3ASKPIQZaa3Ly9qOrarHNpU9yUy658RM9U.NYALLk87ohTco%2Bf5XWKAfkuHv36HjTqo6Qeahrc7Qck",
#                         "type": "text"
#                     },
#                     {
#                         "key": "Referer",
#                         "value": "http://test.portal.jlncjy.cacfintech.com/",
#                         "type": "text"
#                     },
#                     {
#                         "key": "User-Agent",
#                         "value": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
#                         "type": "text"
#                     }
#                 ],
#                 "body": {
#                     "mode": "raw",
#                     "raw": "{\r\n    \"username\":\"18701079606\",\r\n    \"password\":\"020011\",\r\n    \"verifyCode\": \"4348\"\r\n}"
#                 },
#                 "url": {
#                     "raw": "http://api//api/v1.0/chanquan/user/login",
#                     "host": [
#                         "http://api/"
#                     ],
#                     "path": [
#                         "api",
#                         "v1.0",
#                         "chanquan",
#                         "user",
#                         "login.yaml"
#                     ]
#                 }
#             },
#             "response": []
#         }
#     ],
#     "event": [
#         {
#             "listen": "prerequest",
#             "script": {
#                 "id": "b66cb7c2-f925-4908-8277-192db0c0a73d",
#                 "type": "text/javascript",
#                 "exec": [
#                     ""
#                 ]
#             }
#         },
#         {
#             "listen": "test",
#             "script": {
#                 "id": "0ef04a23-f03c-48c1-85da-576e263497ca",
#                 "type": "text/javascript",
#                 "exec": [
#                     ""
#                 ]
#             }
#         }
#     ],
#     "variable": [
#         {
#             "id": "8be17dc6-4b43-4a23-b0f9-ddcf8b440203",
#             "key": "stage",
#             "value": "por.jlncjy.cacfintech.com"
#         },
#         {
#             "id": "790e57d9-c7d0-455c-9ab1-615678ab56d7",
#             "key": "test",
#             "value": "test.por.jlncjy.cacfintech.com"
#         }
#     ],
#     "protocolProfileBehavior": {}
# }
# # json.dumps(字典)：将字典转为JSON字符串
# json_dict=json.dumps(dict1)
# #print(json_dict)
#
# # 行缩进和键值排序
# json_dict_2 = json.dumps(json_dict, indent=2, sort_keys=True, ensure_ascii=False)
# #print(json_dict_2)
#
# #json.loads(json串)，将json字符串转化成字典
# dict_from_str = json.loads(json_dict_2)
# #print(type(dict_from_str))
#
# # dict_from_str_2 = json.loads(json_dict_2)
# # print(dict_from_str_2)
#
# #json.dump，把字典转换成json字符串并存储在文件中
#
# with open("A.json", "w", encoding='utf-8') as f:
#       json.dump(dict1, f)  # 写为一行
#      #json.dump(dict_from_str, f, indent=2, sort_keys=True, ensure_ascii=False)  # 写为多行
#
#列表循环
def inx(*args,**kwargs):
    age = 18
    s=[lambda age:age for i in e]
    print(s[0](1))
    print(s[0](2))
    print(s[0](3))

if __name__ == '__main__':
    e = ([1, 2, 3])
    inx(e)