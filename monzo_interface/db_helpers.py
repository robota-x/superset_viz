from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import create_database, database_exists

from .models import Base  # same instance inherited from the models


config = ConfigParser()
config.read("config.ini")

database_location = config['DATABASE']['location']


def cache_get_engine():
    engine = None

    def get_engine():
        nonlocal engine
        if not engine:
            engine = create_engine(database_location, echo=False)
        return engine

    return get_engine


get_engine = cache_get_engine()


def get_session():
    return sessionmaker(bind=get_engine())()


def initialize_database():
    if not database_exists(database_location):
        print('database not found, creating it...')
        create_database(database_location)
    
    engine = get_engine()

    Base.metadata.create_all(engine)


def get_or_create_by_id(Model, session, id=None, **kwargs):
    id = id or kwargs.pop("id")
    entry = session.query(Model).filter(Model.id == id).first()

    if not entry:
        entry = Model(id=id, **kwargs)
        session.add(entry)

    return entry
