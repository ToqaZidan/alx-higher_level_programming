#!/usr/bin/python3
"""
Module that contains the class definition of a State and an instance
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Class definition of a State and an instance

    Attributes:
        __tablename__: table name
        id: id of the state (INT)
        name: name of the state (String)
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
