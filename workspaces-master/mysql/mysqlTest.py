

import pymysql
#mysql查询
def connMySQL():
    try:
        conn=pymysql.Connect(host='127.0.0.1',
                             user='root',
                             passwd='123456',
                             db='five')
    except Exception as e:
        return e.args
    else:
        #创建游标之后，进行增删改查的操作
        cur=conn.cursor()
        #sql='select * from user where id=%s'
        #将params的值传进了sql的占位符
        #params=(1,)
        #单条语句查询
        # cur.execute(sql,params)
        # data=cur.fetchone()
        # print(data)
        #批量查询
        cur.execute('select * from user')
        data=cur.fetchall()
        #返回类型是元祖
        for i in data:
            print(i)
        #返回列表推导式 学习一下
        db=[item for item in data]
        print(db)
#需要关闭连接池
    finally:
        #游标关闭
        cur.close()
        #链接关闭
        conn.close()

#mysql插入
def insetMySQL():
    try:
        conn=pymysql.Connect(host='127.0.0.1',
                             user='root',
                             passwd='123456',
                             db='five')
    except Exception as e:
        return e.args
    else:
        #创建游标之后，进行增删改查的操作
        cur=conn.cursor()
        #单条插入
        # sql='insert into user values (%s,%s,%s,%s)'
        # params=(6,'yangyang',19,'nanjing')
        #cur.execute(sql,params)
        #批量插入
        sql = 'insert into user values (%s,%s,%s,%s)'
        params=[
                (7,'yangyang',19,'nanjing'),
                (8, 'yangyang', 19, 'nanjing')
                ]
        cur.executemany(sql,params)
        #提交
        conn.commit()
#需要关闭连接池
    finally:
        #游标关闭
        cur.close()
        #链接关闭
        conn.close()

#update
def update():

    try:
        conn=pymysql.Connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            db='five'
        )

    except Exception as e:
        return e.args

    else:
        cur=conn.cursor()
        sql='update user set age=201 where id=1'
        cur.execute(sql)

    finally:
        conn.close()
        cur.close()

#delete
def deleteMySQL():
    try:
        conn=pymysql.Connect(host='127.0.0.1',
                             user='root',
                             passwd='123456',
                             db='five')
    except Exception as e:
        return e.args
    else:
        #创建游标之后，进行增删改查的操作
        cur=conn.cursor()
        sql='delete from user where id=%s'
        params=(7,)
        cur.execute(sql,params)
        conn.commit()
#需要关闭连接池
    finally:
        #游标关闭
        cur.close()
        #链接关闭
        conn.close()

class MysqlHelper():

    def conn(self):
        con=pymysql.Connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            db='five')
        return con
    #创建游标和查询
    def selete_one(self, sql, params):
        cur=self.conn().cursor()
        data=cur.execute(sql,params)
        result=cur.fetchone()
        return result

def checkvaild(username,password):
    opera=MysqlHelper()
    sql='select * from login.yaml where username=%s and password=%s'
    params=(username,password)
    return opera.selete_one(sql=sql,params=params)

def info():
    username=input('请输入用户名：\n')
    password=input('请输入密码：\n')
    result=checkvaild(username,password)
    if result:
        print('登录成功，昵称：{0}'.format(username))
    else:
        print('登陆失败，请检查用户名和密码')
if __name__ == '__main__':
    info()

#封装类
'''
class MysqlHelper():

    def __init__(self,sql,params):
        self.sql=sql
        self.params=params

    def conn(self):
        con=pymysql.Connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            db='five')
        return con
    #创建游标和查询
    def selete_one(self, sql, params):

        cur=self.conn().cursor()
        data=cur.execute(sql,params)
        result=cur.fetchone()
        return result

class my(object):

    def __init__(self, sql, params):
        self.sql = sql
        self.params = params

    def checkvaild(self,username,password):
        opera=MysqlHelper('panda','123456')
        sql="select * from login.yaml where username=%s and password=%s"
        params=(username,password)
        result=opera.selete_one(sql=sql,params=params)
        if result:
            print('登录成功')

if __name__ == '__main__':

    m=my('panda','123456')
    m.checkvaild('panda','123456')
'''