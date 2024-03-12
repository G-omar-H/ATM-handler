#!/usr/bin/python3
"""
        storage data engine
        MySQL DataBase
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.atm import ATM
from models.atmdevice import AtmDevice
from models.branch import Branch
from models.device import Device
from models.event import Event
from models.region import Region
from models.electrinicjournal import ElectronicJournal
from models.transaction import Transaction
from models.group import Group

class DBStorage:
    """
    mysql database engine class orm
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initialization...
        """
        self.__engine = create_engine("mysql://{}:{}@{}/{}".format(
             getenv("DB_USER"),
                getenv("DB_PASSWORD"),
                getenv("DB_HOST"),
                getenv("DB_NAME"),
            ),
            pool_pre_ping=True, 
        )
        # Create all tables if not exists
        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        all objects depending of the class name (argument cls)
        """
        obj_dict = {}
        objs_list = [Group, Transaction, ElectronicJournal, Region, Event, Device, Branch, AtmDevice, Atm]
        objs = []
        if cls is not None:
            objs.extend(self.__session.query(cls).all())
        else:
            for table_name in objs_list:
                objs.extend(self.__session.query(table_name).all())
        for obj in objs:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        """
        add the object to the current database session.
        """
        self.__session.add(obj)
        self.__session.flush()

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and the current database session
        """
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def load_from_json(self, filename="dummy.json"):
        """
        Load data from a JSON file and insert into the database.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: JSON file {filename} not found!")
            return

        # Iterate through each table in the JSON data
        for table_name, table_data in data.items():
            # Get the corresponding table model class
            table_model = getattr(sys.modules[__name__], table_name)

            # Insert data into the table
            for row in table_data:
                self.__session.merge(table_model(**row))

        # Commit changes to the database
        self.save()
        print(f"Data successfully populated from JSON file {filename}.")