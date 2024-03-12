#!/usr/bin/python3
"""
Branch model for Branch table
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


class Branch(Base):
  __tablename__ = "Branch"

  branchId = Column(Integer, primary_key=True)
  branchName = Column(String(50))
  regionId = Column(Integer, ForeignKey("Region.id"))

  def __repr__(self):
    return f"Branch(branchId={self.branchId}, \
            branchName='{self.branchName}', \
                regionId={self.regionId})"
