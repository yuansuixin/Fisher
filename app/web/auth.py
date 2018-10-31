from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    user = User.query.filter_by(email=form.email.data)
    if user and user.check_password(form.password.data):
        login_user(user, remember=True)
        # 存储的是一次性的cookie，关闭浏览器的时候就自动清空了,加上remember就可以成为长期的cookie，过期时间默认是365天
        #如果实现更改过期时间，可以在配置里配置
        next = request.args.get('next')
        if not next and next.startwith('/'):   # 防止重定向攻击
            next = url_for('web.index')
        return redirect(next)
    else:
        flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
