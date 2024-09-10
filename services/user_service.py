from sqlalchemy import Select
from models.user_model import UserModel,db

class UserService: 
    @staticmethod
    def login(username:str, password:str):
        query = Select(UserModel).where(UserModel.username == username)
        # 如果用户不存在则会返回None，不会抛出异常
        user_model = db.session.scalars(query).first()
        if user_model and user_model.password == password:
            return user_model
        else:
            return None