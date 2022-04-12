#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ as env
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity',
                      metadata=Base.metadata,
                      Column('place_id',
                             ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id',
                             ForeignKey('amenities.id'),
                             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    if env.get('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review',
                               backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity',
                                 secondary=place_amenity)
    else:
        from models import storage

        @property
        def reviews(self):
            """getter for FileStorage"""
            objs = []
            for key, value in storage.all('Review').items():
                if value.place_id == self.id:
                    objs.append(value)
            return objs

        @property
        def amenities(self):
            objs = []
            for key, value in storage.all('Amenity').items():
                if value.place_id == self.id:
                    objs.append(value)
            return objs

    amenity_ids = []
