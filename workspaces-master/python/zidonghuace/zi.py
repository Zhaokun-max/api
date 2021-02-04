
#获取列表中某个字段的值
dict1 = {"content":{"pageNo":1,"pageSize":30,"totalPage":10,"expectPositionName":None,
                    "showId":None,"positionList":{"positionId":7875046,"companyId":370487,
                    "positionName":"测试工程师"}}}
print(dict1["content"]["positionList"]["positionName"])


