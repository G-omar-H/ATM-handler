#!/usr/bin/python3
"""
Event model for Event table
"""

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    DECIMAL,
    Table,
    Enum,
)
from sqlalchemy.orm import relationship
from base_model import Base


class Event(Base):
    __tablename__ = "Event"

    eventId = Column(Integer, primary_key=True)
    eventName = Column(String(100), nullable=False, unique=True)
    eventLevel = Column(Enum("INFO", "WARNING", "ERROR", "CRITICAL"),
                        nullable=False)
    ejId = Column(Integer, ForeignKey("ElectronicJournal.ejId"))

    # Relationship with ElectronicJournal table
    electronic_journal = relationship("ElectronicJournal", backref="events")

    def __repr__(self):
        return f"<Event(eventId={self.eventId},\
                eventName={self.eventName}, \
                eventLevel={self.eventLevel}, \
                ejId={self.ejId})>"
