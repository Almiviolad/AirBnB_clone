#!/usr/bin/python3
"""module that cintain review class"""
from models.base_model import BaseModel

class Review(BaseModel):
    """defines review class that inherits from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(*args, **kwargs):
        """class constructor to initialise class"""
        super().__init__(*args, **kwargs)
