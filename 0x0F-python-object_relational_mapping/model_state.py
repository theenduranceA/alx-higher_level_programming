#!/usr/bin/python3
"""Module of class definition of a State and an instance."""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class instance."""

    __tablename__ = "states"

    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True)
    name = Column(String(128), nullable=False)
