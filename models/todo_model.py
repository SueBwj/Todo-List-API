from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# 构建数据库结构
class TodoItem(db.Model):
    __tablename__ = 'Todo'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(128), nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description
        
    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'description':self.description    
        }
    
    


    