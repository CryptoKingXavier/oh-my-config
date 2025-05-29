from flaskapp import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
  __tablename__ = "users"

  uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(20), nullable=False, unique=True, comment="User's Username")
  password = db.Column(db.String(20), nullable=False, unique=True, comment="User's Password")
  notes = db.relationship("Notes", backref="author", lazy=True)

  def __repr__(self):
    return f"<User: {self.username}>"

  def get_id(self):
    return self.uid
