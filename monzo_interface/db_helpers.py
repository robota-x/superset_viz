from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def cache_get_engine():
    engine = None

    def get_engine():
        nonlocal engine
        if not engine:
            print('inst')
            engine = create_engine("sqlite:///db.sqlite", echo=True)
        print('ret')
        return engine

    return get_engine


get_engine = cache_get_engine()


def get_session():
    return sessionmaker(bind=get_engine())


def write_models():
    engine = get_engine()

    Base.metadata.create_all(engine)
