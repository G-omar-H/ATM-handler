#!/usr/bin/python3
"""Branch class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Branch(BaseModel, Base):
    __tablename__ = 'Branch'

    branchId = Column(Integer, primary_key=True)
    branchName = Column(String(50))
    regionId = Column(Integer, ForeignKey('Region.regionId'))