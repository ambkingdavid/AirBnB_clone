#!/usr/bin/env python3
""" A module that contains the User class"""

import re
from models.base_model import BaseModel


class User(BaseModel):
    """ A class that defines a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
