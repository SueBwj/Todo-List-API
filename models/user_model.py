from common.db import db

# 在原先类名为User的基础上加上Model，让类名表意更加清晰
class UserModel(db.Model):
    __tablename__ = 'user'
    
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # username 需要特殊
    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password
        }
    