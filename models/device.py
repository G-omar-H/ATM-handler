#!/usr/bin/python3
"""Device class table"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Device(Base):
    __tablename__ = 'Device'

    deviceId = Column(Integer, primary_key=True)
    deviceName = Column(String(100))