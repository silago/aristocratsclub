from flask import render_template,redirect, request, Module, jsonify
from app.forms import askForm, answerForm
from app.models import Question, Category, Answer
from datetime import datetime
from flask.ext import login 
from app import db
from app import cfg
from werkzeug.utils import secure_filename
import os,time,datetime

questions = Module(__name__)

@questions.route("/question/<alias>/")
def question(alias):
    form = answerForm()
    question = Question.query.filter(Question.alias==alias).first()
    answers = Answer.query.filter(Answer.question==question.id)
    return render_template('questions/question.html',question=question,answers=answers,form=form)

@questions.route("/category/<alias>/")
def list(alias):
    questions = Question.query.filter(Question.category==category_id)
    return render_template('questions/inCategory.html',questions=questions)

@questions.route("/answer/<question_id>/",methods=['GET','POST'])
def answer(question_id):
    form = answerForm()
    question_alias = Question.query.filter(Question.id==question_id).first().alias
    if form.validate_on_submit():
        item = Answer()
        form.populate_obj(item)
        item.author = login.current_user.get_id()
        item.question = question_id
        db.session.add(item)
        db.session.commit()
    return redirect('/question/'+question_alias+'/')    


@questions.route("/categories/")
def index():
    categories = Category.query.all()
    return render_template('questions/index.html',categories=categories)


@questions.route("/questions/ask",methods=['GET','PUT']) 
def ask():
    data = request.get_json()
    question = Question()
    for k,o in data.iteritems():
        setattr(question,k,o)
    db.session.add(question)
    db.session.commit()
    return jsonify({})
