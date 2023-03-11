#!/usr/bin/python3
"""module that contains amenity"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """definition of Amenity class that inherits from Basemodel"""
    name = ""

    def __init__(*args, **kwargs):
        """initialises the class"""
        super().__init__(*args, **kwargs)
