#!/usr/bin/python3
"""
main ATM class table
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Atm(BaseModel, Base):
    """
    Main ATM class table

    Args:
        BaseModel (class): base class
        Base (object): declarative instance
    """
    __tablename__ = "ATM"
    
    atmId = Column(Integer, primary_key=True)
    atmName = Column(String(45))
    networkAddress = Column(String(45))
    latitude = Column(Float)
    longitude = Column(Float)
    timezone = Column(DateTime)
    subnet = Column(String(45))
    branchId = Column(Integer, ForeignKey('Branch.branchId'))
    groupId = Column(Integer, ForeignKey('Group.groupId'))

    branch = relationship("Branch", backref="atms")
    group = relationship("Group", backref="atms")