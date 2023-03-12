#!/usr/bin/env python3
"""This module contains the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """a class that defines Review"""

    text = ""
    user_id = ""
    place_id = ""
