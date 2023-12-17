#!/usr/bin/python3
"""the class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """this is the class State"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
