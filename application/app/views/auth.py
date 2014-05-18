from flask.ext.admin.contrib.sqla import ModelView
from wtforms.fields import SelectField, FileField
from flask.ext.admin.model.template import macro
from flask import render_template, request, Module, redirect
#ifrom app import app
from app.forms import regForm, authForm
from app.models import User,Category
from app import db
import hashlib
from app import cfg
from werkzeug.utils import secure_filename
import os,time,datetime
from flask.ext.admin import AdminIndexView, Admin, BaseView, expose
from flask.ext import login 
from PIL import Image


auth = Module(__name__)

@auth.route("/auth/logout/")
@login.login_required
def logout():
    login.logout_user()
    return redirect('/')

@auth.route("/auth/login/",methods=['GET','POST']) 
def logIn():
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
        print 1
        filename=''
        dt = time.mktime(datetime.datetime.now().timetuple())
        file = request.files['img']
        if file:
            filename=str(dt)+"_"+secure_filename(file.filename)
            path = os.path.join(cfg['UPLOAD_FOLDER'],filename)
            path_thumb = os.path.join(cfg['UPLOAD_FOLDER'],'thumb_'+filename)
            file.save(path)
            thumb = Image.open(path)
            if thumb.size[0]<thumb.size[1]: thumb = thumb.transform((thumb.size[0],thumb.size[0]),Image.EXTENT,(0,0,thumb.size[0],thumb.size[0]))
            else:                           thumb = thumb.transform((thumb.size[1],thumb.size[1]),Image.EXTENT,(0,0,thumb.size[1],thumb.size[1]))
                
            
            thumb.thumbnail((300, 300), Image.ANTIALIAS)
            thumb.save(path_thumb)
        model.img = filename
        pass

class AdmIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect('/auth/login')
        return super(AdmIndexView, self).index()
