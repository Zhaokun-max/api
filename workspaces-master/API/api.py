from flask import Flask,jsonify
from flask_restful import Api,Resource,reqparse

app=Flask(__name__)
api=Api(app)

class LoginView(Resource):
    def get(self):
        return {'status':0,'mas':"ok",'data':'this is a login.yaml page'}

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help='您输入的用户名不能为空')
        parser.add_argument('password',type=str,required=True,help='密码不能为空')
        parser.add_argument('age',type=int,help='年龄必须为整数')
        parser.add_argument('sex',type=str,help='性别只能是男或女',choices=['男','女'])
        args=parser.parse_args()
        return jsonify(args)

api.add_resource(LoginView,'/login',endpoint='login')

if __name__ == '__main__':
    app.run(debug=True)