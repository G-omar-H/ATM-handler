#!/usr/bin/python3
"""ATMDevice class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class ElectronicJournal(BaseModel, Base):
    __tablename__ = 'ElectronicJournal'

    ejId = Column(Integer, primary_key=True)
    ejData = Column(String(1000))
    atmId = Column(Integer, ForeignKey('ATM.atmId'))