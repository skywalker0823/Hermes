from .db import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # C
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # R
    def select_by_name(cls,name):
        return cls.filter_by(username=name).first()

    # U
    def update(self):
        db.session.commit()

    # D
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    