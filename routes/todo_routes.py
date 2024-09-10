from flask import Blueprint
from flask_restful import Api
from resources.todo_resources import TodoListResources, TodoResources


todo_bp = Blueprint('todo_bp', __name__)
api = Api(todo_bp)

api.add_resource(TodoResources,'/todos/<int:todo_id>')
api.add_resource(TodoListResources,'/todos')