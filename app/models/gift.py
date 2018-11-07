# -*- coding: utf-8 -*-
from collections import namedtuple

from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook

# EachGiftWishCount = namedtuple('EachGiftWishCount', ['count','isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship("User")
    # 这个user是变量名user
    uid = Column(Integer, ForeignKey('user.id'))
    launched = Column(Boolean, default=False)
    isbn = Column(String(15), nullable=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls,isbn_list):
        # 根据传入的一组isbn， 到gift表中检索出相应的礼物，并且计算出某个礼物
        # 的wish心愿数量
        # 参数需要为条件表达式
        # 分组统计，跨表查询使用db.session.query是更好的
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                      Wish.isbn.in_(isbn_list),
                                      Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count':w[0], 'isbn':w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物，具体
    # 类代表礼物这个事物，他是抽象的
    @classmethod
    def recent(cls):
        # 链式调用
        # 主体 Query对象
        # 子函数 都会返回主体
        recent_gift = Gift.query.filter_by(launched=False).group_by(
            Gift.isbn).order_by(desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift

    # @classmethod
    # def get_wish_counts(cls, isbn_list):
    #     count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
    #                                                                          Wish.isbn.in_(isbn_list),
    #                                                                          Wish.status == 1).group_by(Wish.isbn).all()
    #     count_list = [EachGiftWishCount(w[0], w[1]) for w in count_list]
    #     return count_list
