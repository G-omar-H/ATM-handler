#!/usr/bin/python3
"""
ATM model for ATM table
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


class ATM(Base):
    __tablename__ = "ATM"

    atmId = Column(Integer, primary_key=True)
    atmName = Column(String(45))
    networkAddress = Column(String(45))
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(String(100))
    subnet = Column(String(45))
    branchId = Column(Integer, ForeignKey(Branch.branchId))
    groupId = Column(Integer, ForeignKey(Group.groupId))
    status = Column(String(20), default="Online")
    cash_level = Column(DECIMAL(10, 2))
    last_cash_replenishment = Column(String(100))
    software_version = Column(String(50))
    uptime = Column(Integer)

    # Relationship with AtmDevice
    devices = relationship("AtmDevice", backref="atm")

    def __repr__(self):
        return f"ATM(atmId={self.atmId}, \
                atmName='{self.atmName}', \
                branchId={self.branchId}, \
                groupId={self.groupId})"
