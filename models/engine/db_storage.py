#!/usr/bin/python3

"""
Populating the master db
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

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
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
             getenv("USER"),
                getenv("PWD"),
                getenv("HOST"),
                getenv("DB"),
            ),
            pool_pre_ping=True, 
        )

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

    def close(self):
        """
        close a connected  session
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        self.__session.close()
