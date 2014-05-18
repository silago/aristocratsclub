from app.models import Tag
from flask import render_template



def tags():
  def tagsMenu():
    tags = Tag.query.all()
    return tags
  return dict(tagsMenu=tagsMenu())

#@boobs.context_processor
#def tagsMenu():
#    return dict(foo=123)

