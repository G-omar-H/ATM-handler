#!/usr/bin/python3
"""
Region model for Region table
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


class Region(Base):
  __tablename__ = "Region"

  id = Column(Integer, primary_key=True)
  regionName = Column(String(50))

  def __repr__(self):
    return f"Region(id={self.id}, regionName='{self.regionName}')"
