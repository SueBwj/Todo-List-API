from flask_sqlalchemy import SQLAlchemy

# flask_restful 期望全局使用一个统一的db
db = SQLAlchemy()