# -*- coding: utf-8 -*-

# sqlalchemy第三方包
# Flask_SQLAlchemy
# Flask的路由是封装的werkzeug而形成的自己的路由系统
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True   # 这样sqlalchemy就不会创建base表了
    # create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)



