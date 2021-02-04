import requests
import ddt
import unittest



def getHeaders():
        headers={
            'Content-Type':'application/json;charset=UTF-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'referer':'https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96?oquery=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&fromSearch=true&labelWords=relative',
            'Cookie':'user_trace_token=20201114162118-4dbdac7c-8feb-44fa-ac64-c39c2d50e86f; _ga=GA1.2.1968805265.1605342074; LGUID=20201114162119-2e0638d3-659a-4fbc-a998-749e61906ef5; LG_HAS_LOGIN=1; RECOMMEND_TIP=true; index_location_city=%E5%8C%97%E4%BA%AC; smidV2=202012081319227112d60445aa09ebef0ab8256ab8ca5700445a9bf0a665830; LG_LOGIN_USER_ID=32347842b920edb3984ba18d0a8b2b5aac0c6a1848e24e8b6cdd62bc68d6177f; gate_login_token=26dc7ab97c97979507f4e79f6d4d51144b3b2f3e9737fcfb372df9b09b048313; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; _putrc=345EFCB320874491123F89F2B170EADC; JSESSIONID=ABAAABAABEIABCI89C8CD004DEB350B5725EE359587D454; login.yaml=true; unick=%E4%B8%96%E8%8D%A3; WEBTJ-ID=20210117182353-1770fdf607e441-007f4bdaeb18fc-5c19341b-2073600-1770fdf607f217; LGSID=20210117182354-0f8a4ab1-956f-4103-8ddf-7e55702b06e9; _gid=GA1.2.1109942850.1610879034; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1609253462,1609254613,1610634109,1610879034; TG-TRACK-CODE=index_search; SEARCH_ID=a8a63273c5314ccabfbfe7ffb5c78756; _gat=1; X_HTTP_TOKEN=4fd8f6c762f039cf9671880161b4cf6b470d2ef13d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219858253%22%2C%22first_id%22%3A%2217640ca59431ca-082b486f22d4ce-3b3d5203-2073600-17640ca59444ed%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baidujava%22%2C%22%24latest_utm_medium%22%3A%22sspc%22%2C%22%24latest_utm_term%22%3A%22java3214%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2287.0.4280.88%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%22175c5d9220220e-013cdeeab52e58-58143518-2073600-175c5d922032e3%22%7D; LGRID=20210117190930-5c6f197d-e3fa-4377-89cf-a5c362ac719f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1610881770'

        }
        return headers

def f():
    t=[i for i in range(1,31)]
    print(t)

@ddt.ddt
class LaGou(unittest.TestCase):
    #元组数据
    @ddt.data((1,),(2,),(3,),(4,),(5,),(6,),(7,),(8,),(9,),(10,))
    # #解压数据
    @ddt.unpack
    def test_laGou(self,page):
        '''请求拉钩'''
        url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
        r=requests.post(url=url,
                        headers=getHeaders(),
                        data={'first':'false','pn':page,'kd':'测试工程师','sid':'ff8dbe6ad7634ce0b30dac8665a680b8'})
        self.assertEqual(r.json()['success'],True)
        print(r.json()['content']['positionResult']['result'][0]['city'])
        print(r.json()['content']['positionResult']['result'][0]['companyFullName'])

if __name__ == '__main__':
    unittest.main(verbosity=2)