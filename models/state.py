#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ as env
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if env.get('HBNB_ENV') == 'db':
        cities = relationship('City',
                              backref='state',
                              cascade="all, delete-orphan")
    @property
    def cities(self):
        """
        getter cities
        """
        from models import storage


        objs = []
        for key, value in storage.all().items():
            key = key.split('.')
            if (key[0] == "City"):
                if (value.state_id == self.id):
                    objs.append(value)
