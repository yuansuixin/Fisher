# -*- coding: utf-8 -*-
from app.libs.http import HTTP
from flask import current_app


class YuShuBook:
    # 模型层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        # url = self.isbn_url
        result = HTTP.get(url)
        #数据可以缓存在数据库中
        self._fill_single(result)

    def _fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def _fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        page = int(page)
        url = YuShuBook.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self._fill_collection(result)

    # 封装成函数并不是代码的多少决定的，而是要考虑代码的可读性

    def calculate_start(self, page):
        return (page-1) * current_app.config['PER_PAGE']
    
    @property
    def first(self):
        return self.books[0] if self.total>=1 else None