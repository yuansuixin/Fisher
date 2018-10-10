# -*- coding: utf-8 -*-
from flask import jsonify, app, Blueprint, request

from app.forms.book import SearchForm
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook

print('id为'+str(id(app))+'的APP注册路由')


@web.route('/book/search')
def search():
    '''
        q: 普通关键字  isbn
        page
    :return:
    '''
    # flask的request是通过代理模式实现的，所以request对象的使用必须在flask上下文环境中使用，
    # 也就是说需要在http请求中使用或者是视图函数中触发，在编写单元测试的时候需要注意，可能得不到我们想要的结果，只是一个LocalProxy，而不是一个request对象
    # q = request.args['q']
    # page = request.args['page']
    # a = request.args.to_dict()  # args是字典的一个子类，因为字典是可变类型，args是不可变类型的，Python里的不可变类型有字符串和元组

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()  # 最好从form里面取出来参数，因为如果没有传值的时候，form里面有设置默认值
        page = form.page.data.strip()

        isbn_or_key = is_isbn_or_key(q)  # 保证视图函数里的代码简介易懂
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)   # flask提供的
        # return json.dumps(result), 200, {'content-type':'application/json'}   python提供的方式
    else:
        return jsonify({'msg':"参数校验失败"})