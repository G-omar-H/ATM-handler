#!/usr/bin/python3
"""
AtmDevice model for AtmDevice table
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


class AtmDevice(Base):
    __tablename__ = "AtmDevice"

    atmId = Column(Integer, ForeignKey(ATM.atmId), primary_key=True)
    deviceId = Column(Integer, ForeignKey(Device.deviceId), primary_key=True)
    deviceStatus = Column(String(20))

    def __repr__(self):
        return f"AtmDevice(atmId={self.atmId}, \
                deviceId={self.deviceId}, \
                deviceStatus='{self.deviceStatus}')"
