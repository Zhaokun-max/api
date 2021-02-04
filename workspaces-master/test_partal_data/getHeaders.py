import pytest

class Get_headers():
    #发布中1.2步使用
    @property
    def getheaders(self):
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'test.rongxin.chanquan.portal.jilin.sid=s%3Atest.rongxin.chanquan.portal.jilin.sid%3ASKPIQZaa3Ly9qOrarHNpU9yUy658RM9U.NYALLk87ohTco%2Bf5XWKAfkuHv36HjTqo6Qeahrc7Qck',
            'Referer': 'http://test.portal.jlncjy.cacfintech.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHAiOiJQQyIsInN1YiI6Ijg2IiwiYXVkIjoicm9uZ3hpbjpjaGFucXVhbjpqd3Q6YWNjZXNzIiwic2NvcGUiOiJ0ZXN0OnJvbmd4aW46Y2hhbnF1YW4iLCJpc3MiOiJST05HWElOX0NIQU5RVUFOIiwidHlwZSI6MywiZXhwIjoxNjEzODE0ODU4LCJvd3QiOiJ1c2VyIiwidXNlckNvZGUiOiJQMjAxMDE0MDAwMDYifQ.gRZxZSO6sQpul2OZMiRfJ3MYzA9hEgh4ouiA5N4Yl1M'
        }
        return headers
    #第三步使用
    @property
    def getheaders_002(self):
        cookies={'Cookie': 'test.rongxin.chanquan.portal.jilin.sid=s%3Atest.rongxin.chanquan.portal.jilin.sid%3ASKPIQZaa3Ly9qOrarHNpU9yUy658RM9U.NYALLk87ohTco%2Bf5XWKAfkuHv36HjTqo6Qeahrc7Qck'}
        return cookies
