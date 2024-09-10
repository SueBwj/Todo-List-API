from flask import Blueprint
from flask_restful import Api
from resources.user_resources import LoginResource


user_bp = Blueprint('user_bp', __name__)
api = Api(user_bp)

api.add_resource(LoginResource,'/login')