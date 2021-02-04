import pytest
import pymysql
#思路  连接数据库  登录  断开

@pytest.fixture()
def connSQL():
    conn=pymysql.connect(host='localhost',user='root',passwd='12356',db='db')
    return coon

def closeSql():
    connSQL.close()

@pytest.fixture()
def init(connSQL):
    connSQL
    yield
    closeSql(connSQL)


def test_get_one(init,connSQL):
    cursor=connSQL.cursor()
    cursor.execute('select * from user;')
    print(cursor.fetchall())
