from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.models.base import db
from app.models.gift import Gift
from app.view_models.gift import MyGifts
from app.view_models.trade import MyTrades
from . import web
__author__ = '七月'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list():
        # 事务，保证程序代码的一致性
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id   # 这个地方的current_user，取决于model中设置了get_user，cookie中的uid转化成了user模型
            # current_user.beans += 0.5
            current_user.beans += current_app.config['BASE_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            # db.session.commit()
        # except Exception as e:  # 避免提交失败，
        #     db.session.rollback()
        #     raise e
    else:
        #ajax
        flash('这本书已经添加到您的清单或者已存在于您的心愿清单')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



