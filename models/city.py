#!/usr/bin/python3
"""module containing city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class definition that inherits from base_model"""
    state_id = ""
    name = ""
