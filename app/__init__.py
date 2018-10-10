# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # 参数是配置的路径，目前是同一级，所以就是config本身
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
