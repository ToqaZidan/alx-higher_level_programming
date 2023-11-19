#!/usr/bin/python3
"""
Module that contains the class definition of a City and an instance
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    Class definition of a State and an instance

    Attributes:
        __tablename__: table name
        id: id of the state (INT)
        name: name of the state (String)
        state_id: city's state id
    """

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
