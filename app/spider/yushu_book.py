# -*- coding: utf-8 -*-
from app.libs.http import HTTP
from flask import current_app


class YuShuBook:
    # 模型层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        # url = self.isbn_url
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, cls.per_page, cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    # 封装成函数并不是代码的多少决定的，而是要考虑代码的可读性
    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']
