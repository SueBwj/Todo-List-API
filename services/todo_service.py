from models.todo_model import TodoItem, db

class TodoService:
    # 使用static是因为这些method都是不依赖于任何的实例或对象
    @staticmethod
    def get_item(todo_id):
        todo = TodoItem.query.get(todo_id)
        return todo.to_dict()
    
    @staticmethod
    def get_todolist(page=1, limit=10):
        # limit 表示每一页最多显示的 todo 项目（item）的个数。
        # 计算跳过的数目
        offset = (page - 1) * limit
        # 获取总数
        total = TodoItem.query.count()
        # 获取指定页数的数据
        todos = TodoItem.query.offset(offset).limit(limit).all()
        todos = TodoItem.query.all()
        return {'data': [todo.to_dict() for todo in todos],'page':page,'limit':limit, 'total':total}
    
    @staticmethod
    def create(title, description):
        todo = TodoItem(title, description)
        db.session.add(todo)
        db.session.commit()
        return todo.to_dict()
    
    @staticmethod
    def update(todo_id,title,description):
        # get()通过主键获取对应的item
        todo = TodoItem.query.get(todo_id)
        todo.title = title
        todo.description = description
        return todo.to_dict()
    
    @staticmethod
    def delete(todo_id):
        todo = TodoItem.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        return todo.to_dict()
        
    