from flask_restful import Resource,reqparse
import jwt
from services.user_service import UserService
from common.constants import LOGIN_SECRET


parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='username can not be empty')
parser.add_argument('password', type=str, required=True, help='user password can not be empty')


class LoginResource(Resource):
    
    def post(self):
        try:
            args = parser.parse_args()
            username = args['username']
            password = args['password']
            
            user_model = UserService.login(username, password)
            if user_model:
                # 使用user_json表示信息转化为了json形式
                user_json = user_model.to_dict()
                jwt_token = jwt.encode(user_json, LOGIN_SECRET, algorithm='HS256')
                user_json['token'] = jwt_token
                
                return user_json, 200
            else:
                return {'error':'Username or password error'}, 401
        
        except Exception as error:
            print('error occur')
            return {'error': f"{error}"}, 400
        