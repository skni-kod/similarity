from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    data       = db.Column(db.String(10000))
    date       = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id    = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id         = db.Column(db.Integer, primary_key=True)
    ipaddress  = db.Column(db. String(100))
    gender     = db.Column(db.String(10))
    age        = db.Column(db.Integer)
    height     = db.Column(db.Integer)
    weight     = db.Column(db.Integer)
    silhouette = db.Column(db.String(20))
    hair_colour = db.Column(db.String(20))
    facial_hair = db.Column(db.String(20))
    glasses    = db.Column(db.String(20))
    skin_colour = db.Column(db.String(20))
    eye_colour  = db.Column(db.String(20))
    date       = db.Column(db.DateTime(timezone=True), default=func.now())


