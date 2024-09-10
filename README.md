# Todo-List-API

### roadmap.sh backend beginning project
- flask_restful_api
- sqlalchemy
- not implementing user authentication and error handling

### project url
https://roadmap.sh/projects/todo-list-api

flask_rest_tutorial/
│
├── common/                  # 常用工具函数或配置文件
│   └── __init__.py
│   └── config.py            # 数据库配置文件
│
├── models/                  # 数据库模型
│   └── __init__.py
│   └── todo_model.py        # Todo数据模型
│
├── resources/               # 资源 (RESTful API的资源)
│   └── __init__.py
│   └── todo_resource.py     # Todo API资源
│
├── routes/                  # 路由
│   └── __init__.py
│   └── todo_routes.py       # 注册Todo相关的路由
│
├── services/                # 业务逻辑
│   └── __init__.py
│   └── todo_service.py      # 处理Todo业务逻辑
│
├── app.py                  # Flask应用主入口
├── requirements.txt         # 依赖包列表
   

