# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail

from app.models.book import db


login_manage = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 参数是配置的路径，目前是同一级，所以就是config本身
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manage.init_app(app)
    login_manage.login_view = 'web.login'
    login_manage.login_message = "请先登录或注册"

    mail.init_app(app)


    # db.create_all(app=app)
    # 同样的功能,将current_app推入栈中，通过源码可以知道
    # 或者在构造函数中将app传入，db = SQLAlchemy(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
