#!/usr/bin/python3
""" City Module for HBNB project """
from os import environ as env
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if env.get('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place',
                               backref='cities',
                               cascade='all, delete-orphan')
