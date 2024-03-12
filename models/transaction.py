#!/usr/bin/python3
"""
Transaction model for Transaction table
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


class Transaction(Base):
    __tablename__ = "Transaction"

    transactionId = Column(Integer, primary_key=True)
    transactionType = Column(String(45), nullable=False)
    transactionDetail = Column(String(1000))
    ejId = Column(Integer, ForeignKey("ElectronicJournal.ejId"))

    # Relationship with ElectronicJournal table
    electronic_journal = relationship("ElectronicJournal",
                                      backref="transactions")

    def __repr__(self):
        return f"<Transaction(transactionId={self.transactionId}, \
                    transactionType={self.transactionType}, \
                    transactionDetail={self.transactionDetail}, \
                    ejId={self.ejId})>"
