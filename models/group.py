#!/usr/bin/python3
"""
Group model for Group table
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

group_atm = Table(
  "group_atm",
  Base.metadata,
  Column("groupId", Integer, ForeignKey("Group.groupId")),
  Column("atmId", Integer, ForeignKey("ATM.atmId")),
)


class Group(Base):
  __tablename__ = "Group"

  groupId = Column(Integer, primary_key=True)
  groupName = Column(String(100))
  groupDescription = Column(String(5000))
  groupType = Column(Enum("Static", "Dynamic"))

  atms = relationship("ATM", secondary="group_atm", backref="groups", cascade="all, delete, delete-orphan")

  def __repr__(self):
    return (
        f"Group(groupId={self.groupId}, groupName='{self.groupName}', "
        f"groupDescription='{self.groupDescription}', atms={self.atms})"
    )
