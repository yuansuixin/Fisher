# -*- coding: utf-8 -*-
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30)])  # 验证器，可以自定义验证器
    page = IntegerField(validators=[NumberRange(min=1, max=99)],default=1)