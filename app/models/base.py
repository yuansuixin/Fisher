# -*- coding: utf-8 -*-

# sqlalchemy第三方包
# Flask_SQLAlchemy
# Flask的路由是封装的werkzeug而形成的自己的路由系统
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:  # 避免提交失败，
            db.session.rollback()
            raise e


# 重写基类
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'stauts' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True   # 这样sqlalchemy就不会创建base表了
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __int__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

