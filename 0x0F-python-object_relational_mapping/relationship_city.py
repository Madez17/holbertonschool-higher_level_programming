#!/usr/bin/python3
"""Create Model City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """class state inherith from Base"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
