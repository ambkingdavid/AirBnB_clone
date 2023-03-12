#!/usr/bin/env python3
"""This module contains the place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """a class that defines a place"""

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
