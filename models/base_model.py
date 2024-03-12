#!/usr/bin/python3
"""
root base model
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Define the base class
Base = declarative_base()
