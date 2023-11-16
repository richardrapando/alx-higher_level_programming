#!/usr/bin/python3

"""
City model
inheriting from SQLAlchemy Base and links to the MySQL table cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """MySQL database city representation.
    Attributes:
        id (sqlalchemy.Column): city's id.
        name (sqlalchemy.Column): city's name.
        state_id (sqlalchemy.Column): city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
