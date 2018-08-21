# coding:utf8

from flask import Flask
from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint

app = Flask(__name__)
app.debug = True
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(home_blueprint)
