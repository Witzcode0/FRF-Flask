from flask_admin.contrib.sqla import ModelView
from app import admin,db
from app.post.models import Post

class PostView(ModelView):
    can_delete = True
    can_view_details = False
    column_searchable_list = ['title', 'content']
    column_editable_list = ['title', 'content']

admin.add_view(PostView(Post, db.session))