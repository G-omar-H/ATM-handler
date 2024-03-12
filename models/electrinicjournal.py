#!/usr/bin/python3
"""
ElectronicJournal model for ElectronicJournal table
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


class ElectronicJournal(Base):
    __tablename__ = "ElectronicJournal"

    ejId = Column(Integer, primary_key=True)
    ejData = Column(String(1000), nullable=False)
    atmId = Column(Integer, ForeignKey("ATM.atmId"), nullable=False)
    timestamp = Column(String(100), nullable=False)

    # Relationship with ATM table
    atm = relationship("ATM", backref="electronic_journals")

    def __repr__(self):
        return f"<ElectronicJournal(ejId={self.ejId}, \
                        ejData={self.ejData}, atmId={self.atmId}, \
                        timestamp={self.timestamp})>"
