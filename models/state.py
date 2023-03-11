#!/usr/bin/python3
"""module that contains state class"""
from models.base_model import BaseModel

class State(BaseModel):
    """state class tha inherits from Basemodel"""
    name = ""

    def __init__(*args, **kwargs):
        """class constructor to initialise class"""
        super().__init__(*args, **kwargs)


