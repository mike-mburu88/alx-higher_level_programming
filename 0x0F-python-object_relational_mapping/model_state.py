#!/usr/bin/python3
"""a python class that contains a class definition of a state database 
State and inherits from the base class as a declarative class while using Alchemy
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
import sys 

Base = declarative_base()

class State(Base):
    """State class inherits  from base and links 
    to the MySQL table 'states'


    Attributes:
        name: the column with a string of characters(max 128)
        id: column of a unique set of integers that cant be NULL(primary key
"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
