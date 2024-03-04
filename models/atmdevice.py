#!/usr/bin/python3
"""ATMDevice class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class AtmDevice(BaseModel, Base):
    __tablename__ = 'AtmDevice'

    atmId = Column(Integer, ForeignKey('ATM.atmId'), primary_key=True)
    deviceId = Column(Integer, ForeignKey('Device.deviceId'), primary_key=True)
    deviceStatus = Column(String(100))

    atm = relationship("ATM", backref="atm_devices")
    device = relationship("Device", backref="atm_devices")

