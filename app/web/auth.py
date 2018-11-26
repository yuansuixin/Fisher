from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash

from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.base import db
from app.models.user import User
from . import web
from app.libs.email import send_mail

__author__ = '七月'


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
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
        if not next or next.startwith('/'):   # 防止重定向攻击
            next = url_for('web.index')
        return redirect(next)
    else:
        flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            # 没有查询到直接抛出异常
            user = User.query.filter_by(email=account_email).first_or_404()

            send_mail(form.email.data, '重置你的密码', 'email/reset_password.html',
                      user=user, token=user.generate_token())
            flash('一封邮件已发送到你的邮箱' + account_email + '，请及时查收')
            # return redirect(url_for('web.login'))
    return render_template('auth/forget_password_request.html', form=form)


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token,form.password1.data)
        if success:
            flash('你的密码已更新，请使用新密码登陆')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败')
    return render_template('auth/forget_password.html', form=form)


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))