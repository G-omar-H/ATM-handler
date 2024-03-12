#!/usr/bin/python3
"""
initializing models as python packages
"""

from models.atm import ATM
from models.atmdevice import AtmDevice
from models.branch import Branch
from models.device import Device
from models.event import Event
from models.region import Region
from models.electrinicjournal import ElectronicJournal
from models.transaction import Transaction
from models.group import Group
from models.engine import DBStorage
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()