from functools import wraps
from flask import request
import jwt
from common.constants import LOGIN_SECRET


def token_required():
    def check_token(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            jwt_token = request.headers.get('token',None)
            if not jwt_token:
                return {'error':'User unauthorized'},401
            try:
                user_info = jwt.decode(jwt_token, LOGIN_SECRET, algorithms='HS256')
                # jwt.decode() 只验证 token 签名，不会检查其内容是否符合预期。 防御性编程 让你确保 token 的内容是完整且符合业务逻辑的。
                if not user_info or not user_info.get('username',None):
                    return {'error':'User unauthorized'}, 401
            except Exception as error:
                return {'error':"User unauthorized"}, 401
            
            result = f(*args, **kwargs)
            return result
        
        return wrapper
    return check_token