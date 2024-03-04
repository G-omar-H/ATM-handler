#!/usr/bin/python3
"""Transaction class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Group(BaseModel, Base):
    __tablename__ = 'Group'

    groupId = Column(Integer, primary_key=True)
    groupName = Column(String(100))
    groupDescription = Column(String(100))
    groupType = Column(String(45))