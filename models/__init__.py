#!/usr/bin/python3
"""initialises the package"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
