from app import db
import datetime

ROLE_USER = 0
ROLE_ADMIN = 1


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lang = db.Column(db.String(3),)
    name = db.Column(db.String(255),)
    text = db.Column(db.String(255), index=True, unique=True)
    def __repr__(self):
        return '<Menu %r>' % (self.name)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lang = db.Column(db.String(3),)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = True)
    name = db.Column(db.String(255),)
    alias = db.Column(db.String(255), index=True, unique=True)
    def for_api(self):
        return {'id':self.id,'alias':self.alias,'name':self.name}
    def __repr__(self):
        return '<Category %r>' % (self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255),)
    name = db.Column(db.String(255),)
    password = db.Column(db.String(255),)
    img = db.Column(db.String(255),)
    text = db.Column(db.Text(), )
    status = db.Column(db.Integer,)
    city = db.Column(db.String(255),)
    country = db.Column(db.String(255),)
    group = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime)
    def for_api(self):
        return {'id':self.id,'img':self.img,'name':self.name,'city':self.city,'country':self.country,'email':self.email}
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.name
    
    def __repr__(self):
        return '<User %r>' % (self.name)


class Media(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(255),)
    url = db.Column(db.String(255),)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def for_api(self):
        return {'id':self.id,'type':self.type,'url':self.url}
    def __unicode__(self):
        return self.name
    def __repr__(self):
        return '<Media %r>' % (self.url)

class Pic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(255),)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    type = db.Column(db.Integer)
    def __repr__(self):
        return '<Pic %r>' % (self.url)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lang = db.Column(db.String(3),)
    name = db.Column(db.String(255),)
    alias = db.Column(db.String(255), index=True, unique=True)
    text = db.Column(db.Text(), )
    created_at = db.Column(db.DateTime,)
    def __repr__(self):
        return '<Article %r>' % (self.name)

class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lang = db.Column(db.String(3),)
    name = db.Column(db.String(255),)
    alias = db.Column(db.String(255), index=True, unique=True)
    img = db.Column(db.String(255),)
    text = db.Column(db.Text(), )
    status = db.Column(db.Integer,)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        return '<News %r>' % (self.name)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    lang = db.Column(db.String(3),)
    name = db.Column(db.String(255),)
    alias = db.Column(db.String(255), index=True, unique=True)
    img = db.Column(db.String(255),)
    text = db.Column(db.Text(), )
    status = db.Column(db.Integer,)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def for_api(self): 
        return {'id':self.id,'name':self.name,'text':self.text}
    
    def __repr__(self):
        return '<Question %r>' % (self.name)



class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text(), )
    question = db.Column(db.Integer, db.ForeignKey('question.id'))
    author = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        return '<Answer %r>' % (self.name)

