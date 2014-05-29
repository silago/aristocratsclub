from flask.ext.admin.contrib.sqla import ModelView
from wtforms.fields import SelectField, FileField
from flask.ext.admin.model.template import macro
from flask import render_template, request, Module, redirect, json, jsonify
#ifrom app import app
from app.forms import regForm, authForm
from app.models import User,Category, Media
from app import db
import hashlib
from app import cfg
from werkzeug.utils import secure_filename
import os,time,datetime
from flask.ext.admin import AdminIndexView, Admin, BaseView, expose
from flask.ext import login 
from PIL import Image
from app.views import functions as nv_functions

auth = Module(__name__)

@auth.route("/auth/logout/")
@login.login_required
def logout():
    login.logout_user()
    return redirect('/')

@auth.route("/me",methods=['GET','POST'])
def me():
    uid = login.current_user.get_id()
    if (not uid):
        return redirect('/auth/login/')
    user = User.query.filter_by(id=uid).first()
    data = request.get_json()
    print data
    if data.has_key('data'):
        for k,o in json.loads(data['data']).iteritems():
            setattr(user,k,o)
        db.session.add(user)
        db.session.commit()
        return jsonify({'status':'1'})
    
    
    if (request.files.has_key('img')):
        url = nv_functions.fileUpload(request,'img')
        if url:
            item = Media()
            item.url = url
            item.type  = 'img'
            item.user_id = uid
            db.session.add(item)
            db.session.commit()
            return redirect('/me/')
    media = Media.query.filter_by(user_id=uid).filter_by(type='img').all()
    return render_template('auth/profile.html',media=media,user=user)

@auth.route("/auth/login/",methods=['GET','POST']) 
def logIn():
    if login.current_user.is_authenticated():
            return redirect('/')
    form = authForm()
    if form.validate_on_submit():
        item = User.query.filter_by(password=hashlib.md5(form.password.data).hexdigest()).filter_by(email=form.email.data).first()
        if item: login.login_user(item)
    return render_template('auth/reg.html',form=form)

@auth.route("/profile/<user_id>/",methods=['GET','POST'])
def profile(user_id):
    item = User.query.filter_by(id=user_id).first()
    return render_template('auth/profile.html')


@auth.route("/auth/reg/",methods=['GET','POST']) 
def register():
    form = regForm()
    if form.validate_on_submit():
        item = User()
        form.populate_obj(item)
        item.password = hashlib.md5(item.password).hexdigest()
        item.status = 1
        db.session.add(item)
        db.session.commit()
    return render_template('auth/reg.html',form=form)


def Resize():
    pass

class UserAdminView(ModelView):
    form_overrides = dict(group=SelectField, img=FileField)
    edit_template = 'admin/model/edit.html'
    form_args = dict(group=dict(choices=[ (str(i.id) , i.name) for i in  (Category.query.all()) ]))
    form_columns = [ 'email','name','status','group','img']
    def on_model_change(self, form, model, is_created):
        img = nv_functions.fileUpload(request,'img')
        if img: model.img = img

class AdmIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect('/auth/login')
        return super(AdmIndexView, self).index()
