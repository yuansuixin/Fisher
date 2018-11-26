# -*- coding: utf-8 -*-
# 记录生产环境和开发环境不同的配置，记录机密的配置，不上传到git

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'

# Email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PROT = 465
MAIL_USER_SSL = True
MAIL_USER_TSL = False
MAIL_USERNAME = 'aaa@qq.com'
MAIL_PASSWORD = 'fdsafdsa'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书<hello@yushu.im>'