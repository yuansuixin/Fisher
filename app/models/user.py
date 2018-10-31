# -*- coding: utf-8 -*-

from flask_login import UserMixin, login_manager
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base


class User(UserMixin, Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_count = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    _password = Column('password',String(128), nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # flask_login需要一个可以表示用户身份的字段，函数名字是固定的,usermixin里已经定义了，只需要继承就可以了
    # def get_id(self):
    #     return self.id


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))





