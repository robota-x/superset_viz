from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

class Transaction(declarative_base()):

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)

    transaction_id = Column(String)
    created = Column(DateTime)
    description = Column(String)
    amount = Column(Integer)
    currency = Column(String)    

    def __repr__(self):
       return f"<Transaction(id={transaction_id}, amount={amount})>" 

    # def __init__(self):
    #     if not cls.engine:
    #         cls.engine = sqlalchemy.create_engine('sqlite:///db.sqlite', echo=True)

