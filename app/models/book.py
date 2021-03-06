# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String


# mvc架构 业务逻辑最好的都是在model层编写
# Code first解决的是创建数据的问题
# orm 对象关系映射包含的层面更广，包含了数据的创建、查询、更新
from app.models.base import db


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default="未知")
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15),nullable=False,unique=True)
    summary = Column(String(1000))
    image = Column(String(50))


