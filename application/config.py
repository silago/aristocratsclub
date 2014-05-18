# all the imports
import os
basedir = os.path.abspath(os.path.dirname(__file__))
#from flask import Flask, request, session, g, redirect, url_for, \
#     abort, render_template, flash

CSRF_ENABLED = True
SECRET_KEY = 'OBEY'


UPLOAD_FOLDER = os.path.join(basedir, 'app/static/media')
SQLALCHEMY_DATABASE_URI="mysql://root@localhost/aristocratsf"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# configuration

#DATABASE = '/tmp/flaskr.db'
DEBUG = True
#USERNAME = 'admin'
#PASSWORD = 'default'
