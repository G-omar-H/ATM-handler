#!/usr/bin/python3
"""This module defines a base class for all models in our database"""

from sqlalchemy.ext.declarative import declarative_base
from models import storage

Base = declarative_base()

class BaseModel:
    """root class parent"""

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        storage.new(self)
        storage.save()

    def delete(self):
        """
        Delete the current instance from the storage (models.storage)
         by calling the method delete
        """
        from models import storage
        storage.delete(self)
