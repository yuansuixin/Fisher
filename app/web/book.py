# -*- coding: utf-8 -*-
from flask import jsonify, app, request

from app.forms.book import SearchForm
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

print('id为'+str(id(app))+'的APP注册路由')


@web.route('/book/search')
def search():
    '''
        q: 普通关键字  isbn
        page
    :return:
    '''
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()  # 最好从form里面取出来参数，因为如果没有传值的时候，form里面有设置默认值
        page = form.page.data.strip()

        isbn_or_key = is_isbn_or_key(q)  # 保证视图函数里的代码简介易懂
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)   # flask提供的
    else:
        return jsonify(form.errors)
