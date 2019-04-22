from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
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
    postcode = Column(String)
    city = Column(String)
    region = Column(String)
    country = Column(String)
    address = Column(String)
    approximate = Column(Boolean)

    online = Column(Boolean)
    atm = Column(Boolean)

    transactions = relationship("Transaction", back_populates="merchant")

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

    merchant_id = Column(String, ForeignKey("merchants.id"))
    merchant = relationship("Merchant", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, amount={self.amount})>"


class TransactionDenormalized(Base):
    __tablename__ = "transactions_denormalized"

    id = Column(String, primary_key=True)

    description = Column(String)

    created = Column(DateTime)
    settled = Column(DateTime)
    updated = Column(DateTime)

    amount = Column(Integer)
    currency = Column(String)
    include_in_spending = Column(Boolean)

    merchant_id = Column(String)

    merchant_name = Column(String)
    merchant_category = Column(String)
    merchant_logo = Column(String)

    merchant_latitude = Column(Float)
    merchant_longitude = Column(Float)
    merchant_postcode = Column(String)
    merchant_city = Column(String)
    merchant_region = Column(String)
    merchant_country = Column(String)
    merchant_address = Column(String)
    merchant_approximate = Column(Boolean)

    merchant_online = Column(Boolean)
    merchant_atm = Column(Boolean)

    def __repr__(self):
        return f"<TransactionDenormalized(id={self.id}, amount={self.amount}, merchant={self.merchant_name})>"

