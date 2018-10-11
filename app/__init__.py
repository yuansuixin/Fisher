# -*- coding: utf-8 -*-
from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 参数是配置的路径，目前是同一级，所以就是config本身
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
