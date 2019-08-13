#!/usr/bin/python3
"""Create Model Base"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """class state inherith from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    city_relation = relationship("City", cascade="all, delete-orphan",
                                 backref="state")
    name = Column(String(128), nullable=False)
