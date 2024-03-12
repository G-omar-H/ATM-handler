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


class Device(Base):
    __tablename__ = "Device"

    deviceId = Column(Integer, primary_key=True)
    deviceModel = Column(String(100))
    deviceManufacturer = Column(String(100))
    deviceSerialNumber = Column(String(50))

    def __repr__(self):
        return f"Device(deviceId={self.deviceId}, \
                        deviceModel='{self.deviceModel}', \
                        deviceManufacturer='{self.deviceManufacturer}', \
                        deviceSerialNumber='{self.deviceSerialNumber}')"
