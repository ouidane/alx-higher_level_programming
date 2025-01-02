#!/usr/bin/python3
"""Definition of the `state` model."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represent a state in the system.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.

    Relationships:
        cities (list): A list of cities associated with the state.

    Table Name:
        states: The name of the database table for storing states.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
