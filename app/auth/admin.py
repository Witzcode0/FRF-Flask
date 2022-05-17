from flask_admin.contrib.sqla import ModelView
from app.auth.models import User
from app import db, admin 

class UserView(ModelView):
    can_delete = True
    can_view_details = False
    # make columns searchable
    column_searchable_list = ['username', 'email']
    # inline editing
    column_editable_list = ['username', 'email']


admin.add_view(UserView(User, db.session))

