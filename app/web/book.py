# -*- coding: utf-8 -*-
import json

from ansible.modules.database.misc.redis import flush
from flask import jsonify, app, request, render_template, current_app, flash

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()  # 最好从form里面取出来参数，因为如果没有传值的时候，form里面有设置默认值
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)  # 保证视图函数里的代码简介易懂
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            YuShuBook.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return jsonify(books)
        # json.dumps(books, default=lambda o: o.__dict__)

    else:
        flush('搜索的关键字不符合要求')
        # return jsonify(form .errors)
        return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


@web.route('/test')
def test():
    r = {
        'name': None,
        'age': 18
    }
    # data['age']
    r1 = {

    }
    flash('hello,qiyue', category='error')
    flash('hello, jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)


@web.route('/test1')
def test1():
    print(id(current_app))
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')
    return ''




