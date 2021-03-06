# -*- coding: utf-8 -*-
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from wtforms import Form, StringField, PasswordField

from app.models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                 Email(message='')])

    password = PasswordField(validators=[
            DataRequired(message='密码不可以为空，请输入你的密码'), Length(6,32)])

    nickname = StringField(validators=[
        DataRequired(), Length(2,10,message='昵称至少需要两个字符，最多10个')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮件已经被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已经存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(),
        Length(6,32,message='密码长度要在6-20个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')
    ])
    password2 = PasswordField(validators=[
        DataRequired(), Length(6,32)
    ])
