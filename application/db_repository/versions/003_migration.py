from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
question = Table('question', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
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
    post_meta.tables['question'].columns['author'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['question'].columns['author'].drop()
