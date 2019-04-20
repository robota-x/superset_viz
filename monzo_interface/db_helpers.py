from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .models import Base  # same instance inherited from the models


def cache_get_engine():
    engine = None

    def get_engine():
        nonlocal engine
        if not engine:
            engine = create_engine("sqlite:///db.sqlite", echo=False)
        return engine

    return get_engine


get_engine = cache_get_engine()


def get_session():
    return sessionmaker(bind=get_engine())()


def write_models():
    engine = get_engine()

    Base.metadata.create_all(engine)


def get_or_create_by_id(Model, session, id=None, **kwargs):
    id = id or kwargs.pop("id")
    entry = session.query(Model).filter(Model.id == id).first()

    if not entry:
        entry = Model(id=id, **kwargs)
        session.add(entry)

    return entry
