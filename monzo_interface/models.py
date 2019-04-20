from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(String, primary_key=True)

    name = Column(String)
    category = Column(String)
    logo = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)
    postcode = Column(Boolean)
    city = Column(Boolean)
    region = Column(Boolean)
    country = Column(Boolean)
    address = Column(Boolean)

    online = Column(Boolean)
    atm = Column(Boolean)
    approximate = Column(Boolean)

    def __repr__(self):
        return f"<Merchant(id={self.id}, name={self.name})>"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)

    description = Column(String)

    created = Column(DateTime)
    settled = Column(DateTime)
    updated = Column(DateTime)

    amount = Column(Integer)
    currency = Column(String)
    include_in_spending = Column(Boolean)

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount})>"
