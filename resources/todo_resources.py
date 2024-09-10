from flask_restful import Resource, reqparse
from services.todo_service import TodoService
from flask import request

# 获取前端返回的数据中的特定参数
# 
parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='todo title can not be empty')
parser.add_argument('description', type=str, required=True, help='todo description can not be empty')


class TodoListResources(Resource):
    def get(self):
        page = request.args.get('page',default=1, type=int)
        limit = request.args.get('limit',default=10, type=int)
        
        todos = TodoService.get_todolist(page, limit)
        
        return todos
    
    def post(self):
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        new_todo = TodoService.create(title=title,description=description)
        return new_todo


class TodoResources(Resource):
    def get(self, todo_id):
        # 获取单个todo item
        todo = TodoService.get_item(todo_id)
        return todo
        
    
    def put(self, todo_id):
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        
        todo = TodoService.update(todo_id, title, description)
        return {'message':'todo item successfully updated','updated todo item': todo}
    
    def delete(self, todo_id):
        delete_todo = TodoService.delete(todo_id)
        return {'message':'delete todo item successfully!','todo item details': delete_todo}