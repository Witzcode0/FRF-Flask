from app import db

class Post(db.Model):
    uId = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return self.title