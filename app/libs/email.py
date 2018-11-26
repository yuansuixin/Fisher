# -*- coding: utf-8 -*-
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    msg = Message('[鱼书]' + ' '+ subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()  # 真实的核心对象是不受线程id影响的
    thr = Thread(target=send_async_email, args=[app, msg])
    # current_app是代理对象，会受到线程id的影响
    thr.start()
