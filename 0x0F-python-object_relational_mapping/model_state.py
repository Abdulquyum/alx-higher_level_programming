#!/usr/bin/python3
""" define state and inherits from BAse class """

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "hbtn_0e_0_usa"), pool_pre_ping=True)
Base= declarative_base()

class state(Base):
    """ state class with instances """
    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128))

Base.metadata.create_all(engine)
