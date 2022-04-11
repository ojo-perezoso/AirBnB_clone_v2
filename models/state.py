#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ as env
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    if env.get('HBNB_ENV') == 'db':
        cities = relationship('City', backref='state', cascade="all, delete-orphan")
