from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list():
        # 事务，保证程序代码的一致性
        # try:
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id   # 这个地方的current_user，取决于model中设置了get_user，cookie中的uid转化成了user模型
            db.session.add(wish)
            # db.session.commit()
        # except Exception as e:  # 避免提交失败，
        #     db.session.rollback()
        #     raise e
    else:
        #ajax
        flash('这本书已经添加到您的清单或者已存在于您的心愿清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
