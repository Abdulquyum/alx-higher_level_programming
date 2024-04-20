#!/usr/bin/python3
'''
    Define state and inherits from BAse class
    Also includes instances of state like sevearal names
    of different cities
'''

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class state(Base):
    """ class definition of state class with
        its instancesinstances
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128))
