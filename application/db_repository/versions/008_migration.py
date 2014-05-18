from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
article = Table('article', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('lang', String(length=3)),
    Column('name', String(length=255)),
    Column('alias', String(length=255)),
    Column('text', Text),
    Column('created_at', DateTime),
)

menu = Table('menu', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('lang', String(length=3)),
    Column('name', String(length=255)),
    Column('text', String(length=255)),
)

news = Table('news', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('lang', String(length=3)),
    Column('name', String(length=255)),
    Column('alias', String(length=255)),
    Column('img', String(length=255)),
    Column('text', Text),
    Column('status', Integer),
    Column('created_at', DateTime),
)

question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('lang', String(length=3)),
    Column('name', String(length=255)),
    Column('alias', String(length=255)),
    Column('img', String(length=255)),
    Column('text', Text),
    Column('status', Integer),
    Column('category', Integer),
    Column('author', Integer),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['article'].create()
    post_meta.tables['menu'].create()
    post_meta.tables['news'].columns['lang'].create()
    post_meta.tables['question'].columns['lang'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['article'].drop()
    post_meta.tables['menu'].drop()
    post_meta.tables['news'].columns['lang'].drop()
    post_meta.tables['question'].columns['lang'].drop()
