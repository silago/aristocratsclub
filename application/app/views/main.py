from flask import render_template, request, Module, jsonify, json
from flask.ext import login 
#ifrom app import app
#from app.forms import boobsForm
from app import db
from app import models
from app import cfg
from werkzeug.utils import secure_filename
import os,time,datetime
from app.forms import regForm, authForm
import sys
from app.forms import searchForm
main = Module(__name__)



#@boobs.route("/boobs/add/",methods=['GET','POST'])
#def add():
#    form = boobsForm()
#    if form.validate_on_submit():
#        filename=''
#        dt = time.mktime(datetime.datetime.now().timetuple())
#        file = request.files['img']
#        if file:
#            filename=str(dt)+"_"+secure_filename(file.filename)
#            file.save(os.path.join(cfg['UPLOAD_FOLDER'],filename))
#        item = Boob()
#        form.populate_obj(item)
#        item.img = filename
#        db.session.add(item)
#        db.session.commit()
#    return render_template("base/add.html",form=form)

@main.route("/GET/<model>.json",methods=['GET'])
def GET(model):
    options = json.loads(request.args.get('options'))
    filter = '1 ';
    for k,o in options.iteritems(): filter=filter+"and `"+k+"` = '"+str(o)+"'" 
    m = getattr(sys.modules["app.models"], model)
    return jsonify(data=[ i.for_api() for  i in m.query.filter(filter).all()])

@main.route("/POST/<model>/",methods=['POST'])
def POST(model):
    pass

@main.route("/search/",methods=['GET'])
def search():
    form = searchForm()
    return render_template("search.html",form=form)

@main.route("/",methods=['GET','POST'])
def index():
    uid  = login.current_user.get_id()
    current = {'uid':uid}  
    return render_template("index.html",  current=json.dumps(current))

#@app.context_processor
#def generateMenu():
#    return menu;
