#!/usr/bin/python3

""" define state and inherits from BAse class """

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class state(Base):
    """ state class with instances """
    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128))
