#!/usr/bin/ env python3
"""
Module that contains the class definition of a State and an instance
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Class definition of a State and an instance
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
