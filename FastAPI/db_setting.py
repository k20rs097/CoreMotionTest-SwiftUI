from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, scoped_session
from db_model import Base

user_name = 'NAME'
password = 'PASSWORD'
host = 'HOST'
database_name = 'magnetic_field_map'

DATABASE = 'mysql://%s:%s2%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

if not database_exists(ENGINE.url):
    create_database(ENGINE.url)

Base.metadata.create_all(bing=ENGINE)

Base.query = session.query_property()