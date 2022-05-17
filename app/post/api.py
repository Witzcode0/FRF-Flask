from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.post.models import Post
from app.auth.models import User
from app.post.schemas import PostSchema


class PostListApi(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()
        posts = Post.query.filter_by(uId=user.id).all()
        posts_schema = PostSchema(many=True)
        return posts_schema.dump(posts)

    @jwt_required()
    def post(self):
        json_data = request.get_json()
        current_user = get_jwt_identity()
        user = User.query.filter_by(email=current_user).first()
        new_post = Post(
            uId = user.id,
            title = json_data['title'],
            content = json_data['content'],
        )
        db.session.add(new_post)
        db.session.commit()
        post_schema = PostSchema()
        return post_schema.dump(new_post)



class PostDetailApi(Resource):
    def get(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass