from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["SECRET_KEY"] = '571ebf8e13ca209536c29be68d435c00'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:1234@localhost/frf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='FRF', template_mode='bootstrap3')
api = Api(app)
ma = Marshmallow(app)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "72ea0aebb42c45fd0d4e4c1fe162ca69" + "2c0928b4e03c0adb3a967623889d143fd593a1af"

from app.auth.models import User
from app.post.models import Post

from app.auth.admin import UserView
from app.post.admin import PostView

from app.auth.api import UserListApi, UserDetailApi, LoginApi
from app.post.api import PostListApi, PostDetailApi

# register api route
api.add_resource(UserListApi, '/auth/api/v1.0/users', endpoint='users')
api.add_resource(UserDetailApi, '/auth/api/v1.0/user', endpoint="user")

# login api route
api.add_resource(LoginApi, '/auth/api/v1.0/login/', endpoint='login')

# post api route
api.add_resource(PostListApi, '/post/api/v1.0/posts', endpoint='posts')
api.add_resource(PostDetailApi, '/post/api/v1.0/post/<int:id>', endpoint='post')