from flask import Flask
from models.todo_model import db
from routes.todo_routes import todo_bp

app = Flask(__name__)
app.config.from_object('common.config.Config')

db.init_app(app)

with app.app_context():
    db.create_all()



app.register_blueprint(todo_bp)


if __name__ == "__main__":
    app.run(debug=True)