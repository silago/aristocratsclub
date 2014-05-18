# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, FileField, BooleanField, TextAreaField, PasswordField
from wtforms.fields.core import SelectField
from app.models import Category

from wtforms.validators import Required

class searchForm(Form):
    query = TextField('Текст',validators=[Required])


class authForm(Form):
    email = TextField('email', validators=[Required()])
    password = PasswordField('password',validators=[Required()])
    
class regForm(Form):
    email = TextField('email', validators=[Required()])
    name = TextField('name', validators=[Required()])
    password = PasswordField('password',validators=[Required()])

class askForm(Form):
    name = TextField('name', validators=[Required()])
    category = SelectField('Категория', choices = [ [i.id , i.name] for i in  (Category.query.all()) ],coerce=int) 
    text = TextAreaField('text',)
    
class answerForm(Form):
    text = TextAreaField('text', validators=[Required()])

class boobsForm(Form):
    name = TextField('name', validators=[Required()])
    alias = TextField('alias',validators=[Required()])
    img = FileField('img',)
    text = TextAreaField('text',)
    status = TextField('status',)

class tagsForm(Form):
    name = TextField('name', validators=[Required()])
    alias = TextField('alias',validators=[Required()])
    #openid = TextField('openid', validators = [Required()])
    #remember_me = BooleanField('remember_me', default = False)
