from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable= False)
    password = db.Column(db.String(150), nullable = False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return self.email