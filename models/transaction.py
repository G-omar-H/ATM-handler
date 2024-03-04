#!/usr/bin/python3
"""Transaction class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Transaction(BaseModel, Base):
    __tablename__ = 'Transaction'

    transactionId = Column(Integer, primary_key=True)
    transactionType = Column(String(45))
    transactionDetail = Column(String(1000))
    ejId = Column(Integer, ForeignKey('ElectronicJournal.ejId'))