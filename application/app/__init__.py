from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView


""" application launching """
app = Flask(__name__)
login_manager = LoginManager()

app.config.from_object('config')
db = SQLAlchemy(app)
cfg = app.config


from app.views.auth import AdmIndexView
admin = Admin(app, 'Auth', index_view=AdmIndexView())


#login_manager.init_app(app)
def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

init_login()

""" importing app modules """
from app.views.main import main
#from app.views.tags import tags
from app.views.auth import auth, UserAdminView
app.register_module(main)
#app.register_module(tags)
app.register_module(auth)

#from app.models import Boob, Tag, User
from app.models import User, Answer, Question, News
admin.add_view(UserAdminView(User, db.session))
admin.add_view(ModelView(Answer, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(News, db.session))



#from app import forcontext
#app.context_processor(forcontext.tags)
