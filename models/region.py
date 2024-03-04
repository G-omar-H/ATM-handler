#!/usr/bin/python3
"""Region class table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Region(BaseModel, Base):
    __tablename__ = 'Region'

    regionId = Column(Integer, primary_key=True)
    regionName = Column(String(50))