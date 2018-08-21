# coding:utf8
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/movie'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    pwd = db.column(db.String(80))
    phone = db.column(db.String(80), unique=True)
    info = db.column(db.text)
    face = db.column(db.String(255), unique=True)
    reg_time = db.column(db.DateTime, index=True, default=datetime)
    # user unique flag
    uuid = db.column(db.String(225), unique=True)
    user_logs = db.relationship("UserLog", backref="user")

    def __repr__(self):
        return '<User %r>' % self.username


class UserLog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.Integer, primary_key=True)
    login_time = db.column(db.DateTime, index=True, default=datetime)

    def __repr__(self):
        return '<UserLog %r>' % self.id