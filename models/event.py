#!/usr/bin/python3
"""Event class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Event(Base. BaseModel):
    __tablename__ = 'Event'

    eventId = Column(Integer, primary_key=True)
    eventType = Column(String(100))
    ejId = Column(Integer, ForeignKey('ElectronicJournal.ejId'))