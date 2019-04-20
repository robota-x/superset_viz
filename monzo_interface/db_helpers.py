from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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


def get_or_create_by_id(Model, id, **kwargs):
    session = get_session()
    entry = session.query(Model).filter(Model.id == id).first()

    if not entry:
        print('adding')
        entry = Model(id=id, **kwargs)
        session.add(entry)
        session.commit()
    print('returning')
    return entry