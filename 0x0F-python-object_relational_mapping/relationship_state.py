#!/usr/bin/python3
"""
State model
inheriting from SQLAlchemy Base and links to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """MySQL database state representation.
    Attributes:
        __tablename__ (str): MySQL table name to store States.
        id (sqlalchemy.Integer): state's id.
        name (sqlalchemy.String): state's name.
        cities (sqlalchemy.orm.relationship): State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
