from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from exts import db


class My_blog(db.Model):
    __tablename__ = 'my_blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    mkdown_body = db.Column(db.Text, nullable=False)
    html_body = db.Column(db.Text, nullable=False)
    creat_time = db.Column(db.DateTime, default=datetime.now)
    