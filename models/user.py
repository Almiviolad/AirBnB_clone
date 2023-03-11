#!/usr/bin/python3
"""Module for user class"""
from models.base_model import BaseModel

class User(BaseModel):
    """user class that inherits from BaseModel"""
    email=""
    password=""
    first_name=""
    last_name=""

    def __init__(*args, **kwargs):
        """class constructor to initialise class"""
        super().__init__(*args, **kwargs)
