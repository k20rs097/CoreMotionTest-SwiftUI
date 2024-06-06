from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, scoped_session
from db_model import Base

from env import config

URL = config.URL

ENGINE = create_engine(
    URL,
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