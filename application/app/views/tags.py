from flask import render_template
from flask import Module
#ifrom app import app
from app.forms import tagsForm
from app.models import Tag
from app import db

tags = Module(__name__)

@tags.route("/tags/add/",methods=['GET','POST'])
def add():
    form = tagsForm()
    if form.validate_on_submit():
        item = Tag()
        form.populate_obj(item)
        db.session.add(item)
        db.session.commit()
    return render_template("base/add.html",form=form)
