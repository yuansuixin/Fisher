# -*- coding: utf-8 -*-
from flask import Flask, current_app

app = Flask(__name__)

# flask中的上下文   应用上下文 对象  Flask、   请求上下文 对象  Request的封装
# Flask的核心对象  AppContext
# Request请求对象  RequestContext
# flask使用LocalProxy间接的代理了flask request的上下文
# 离线应用，单元测试
# ctx = app.app_context()
# ctx.push()
# a = current_app   # 核心对象
# d = current_app.config['DEBUG']



# with语句,with语句必须实现__exit__  __enter__两个魔法方法

# 实现了上下文协议的对象使用with
# 上下文管理器    AppContext
# 上下文表达式，必须返回一个上下文管理器
with app.app_context():
    a = current_app  # 核心对象
    d = current_app.config['DEBUG']



