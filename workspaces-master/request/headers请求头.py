import requests
import json

'''
查询电话所在地
'''
# data={"mobileCode":"1350000000","userID":""}
# headers={"Content-Type":"application/x-www-form-urlencoded"}
# r=requests.post(url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
#                 data=data,headers=headers)
# print(r.text)


'''
搜索拉勾网
'''
data={"first":True,"pn":"1","kd":"测试工程师"}
headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
         "referer":"https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=",
         "cookie":"user_trace_token=20201114162118-4dbdac7c-8feb-44fa-ac64-c39c2d50e86f; _ga=GA1.2.1968805265.1605342074; LGUID=20201114162119-2e0638d3-659a-4fbc-a998-749e61906ef5; LG_HAS_LOGIN=1; RECOMMEND_TIP=true; index_location_city=%E5%8C%97%E4%BA%AC; smidV2=202012081319227112d60445aa09ebef0ab8256ab8ca5700445a9bf0a665830; PRE_HOST=www.baidu.com; _gid=GA1.2.923243500.1609253440; gate_login_token=ec0c9c798b81a8da4ca39f228b8872bce9fdb9c461d953322b8c8c19a1bc4d98; LG_LOGIN_USER_ID=32347842b920edb3984ba18d0a8b2b5aac0c6a1848e24e8b6cdd62bc68d6177f; _putrc=345EFCB320874491123F89F2B170EADC; JSESSIONID=ABAAAECABFAACEA5D357860B90F64D630F2B8C0AF60073B; login.yaml=true; unick=%E4%B8%96%E8%8D%A3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; WEBTJ-ID=20201229225214-176aefc3af61b5-099b356dfdf4cc-5c19341b-2073600-176aefc3af719b; sensorsdata2015session=%7B%7D; TG-TRACK-CODE=index_search; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1607323834,1609253437,1609253462,1609254613; LGSID=20201229231014-dfdff190-350a-4938-ab8c-f5d0d601f97a; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.0s00000Ekah6nYffOvPqla1IiENg%5FL7Xr4BuUgZL52iI%5F1j1CAzRVsMd-V7g2gNEyR6Q9N1zT0LimWYJJ6FKCMALIIiK1oTSD%5FK2%5FD3wd6PSxMr4oJ%5FJN%5F2thnOcp1a3gLbcrUuqEFzjxHL3PdNR-TkC4zIw%5F0SGPoLN3SigQkO0UfqLYdFe-0rbLjiHicV0G0f50ym%5FoX19Hvl4O%5F4l5%5FT3AAXN.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4VnL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPS0KzmLmqnfKdThkxpyfqnHRznWf3PHRsnsKVINqGujYkn16Ln1TkP0KVgv-b5HDsP1bvnWmv0AdYTAkxpyfqnHDdn1f0TZuxpyfqn0KGuAnqiDF70APzm1Y1rjnkP0%26ck%3D5306.10.134.334.152.305.162.416%26dt%3D1609253435%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26tpl%3Dtpl%5F11534%5F23295%5F19442%26l%3D1522485503%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; X_HTTP_TOKEN=4fd8f6c762f039cf7264529061b4cf6b470d2ef13d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219858253%22%2C%22first_id%22%3A%2217640ca59431ca-082b486f22d4ce-3b3d5203-2073600-17640ca59444ed%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidujava%22%2C%22%24latest_utm_medium%22%3A%22sspc%22%2C%22%24latest_utm_term%22%3A%22java3214%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2287.0.4280.88%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%22175c5d9220220e-013cdeeab52e58-58143518-2073600-175c5d922032e3%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609254626; LGRID=20201229231028-d25b8417-7442-4b7e-89ba-99356fb42a02; SEARCH_ID=9f29ae32d4e444e2b1ab5546b9f947b0",
         "content-type":"application/x-www-form-urlencoded; charset=UTF-8"
         }
params={"city":"%E5%8C%97%E4%BA%AC","needAddtionalResult":False}
r=requests.post(
    url='https://www.lagou.com/jobs/positionAjax.json',
    data=data,
    params=params,
    headers=headers)
#indent返回的是格式化的json文件
print(json.dumps(r.json(),indent=True,ensure_ascii=False))