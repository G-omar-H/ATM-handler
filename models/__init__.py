from base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.atm import Atm
from models.atmdevice import AtmDevice
from models.branch import Branch
from models.device import Device
from models.event import Event
from models.region import Region
from models.electrinicjournal import ElectronicJournal
from models.transaction import Transaction
from models.group import Group

storage = DBStorage()