#!/usr/bin/python3

"""
State model inheriting
from SLQAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """MySQL database state representation

    __tablename__(str): TMySQL table name to store States
    id(sqlalchemy.Integer): state's id
    name(sqlalchemy.String): state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
