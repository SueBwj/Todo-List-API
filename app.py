from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from common.db import db
from routes.todo_routes import todo_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object('common.config.Config')

db.init_app(app)

with app.app_context():
    db.create_all()



app.register_blueprint(todo_bp)
app.register_blueprint(user_bp)


if __name__ == "__main__":
    app.run(debug=True)