#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ as env
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if env.get('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
