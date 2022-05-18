from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

import base64

from app.auth.schemas import UserSchema
from app.auth.models import User
from app import db, session

class UserListApi(Resource):

    def get(self):
        users_schema = UserSchema(many=True)
        users = User.query.all()
        return users_schema.dump(users)
    
    def post(self):
        json_data = request.get_json()
        exist_email = User.query.filter_by(email=json_data['email']).first()
        print(exist_email)
        if exist_email:
            return "THE EMAIL ADDRESS YOU HAVE ENTERED IS ALREADY REGISTERED"
        else:
            new_user = User(
                username = json_data['username'],
                email = json_data['email'],
                password = base64.b64encode(json_data['password'].encode("ascii")).decode("ascii")
            )
            session.add(new_user)
            session.commit()
            user_schema = UserSchema()
            return user_schema.dump(new_user)
        
        
class UserDetailApi(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()
        user_schema = UserSchema()
        return user_schema.dump(user)

    @jwt_required()
    def put(self):
        current_user = get_jwt_identity()
        json_data = request.get_json()
        user = User.query.filter_by(email=current_user).first()
        if user:
            user.username = json_data['username']
            user.email = json_data['email']
            user.password = json_data['password']
        else:
            user = User(id=id, **json_data)
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return user_schema.dump(user)

    @jwt_required()
    def delete(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()
        if user:
            user.deleted = True
        db.session.add(user)
        db.session.commit()
        return 'your account deleted successfully', 204


class LoginApi(Resource):
    def post(self):
        json_data = request.get_json()
        user = User.query.filter_by(email=json_data['email']).first()
        if json_data['email'] != user.email or json_data['password'] != base64.b64decode(user.password.encode("ascii")).decode("ascii"):
            return "Bad email and password"
        access_token = create_access_token(identity=user.email)
        return {'access_token':access_token}

