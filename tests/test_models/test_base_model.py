#!/usr/bin/env python3

import os
import sys
import models
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestBaseModel_instance(unittest.TestCase):
    def test_instance(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_id_instance(self):
        self.assertIsInstance(BaseModel().id, str)

    def test_unique_id(self):
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_created_at(self):
        f = "%Y-%m-%dT%H:%M:%S"
        obj = datetime.strftime(BaseModel().created_at, f)
        date = datetime.strftime(datetime.today(), f)
        self.assertEqual(obj, date)

    def test_created_at_diff_instance(self):
        f = "%Y-%m-%dT%H:%M:%S"
        obj1 = datetime.strftime(BaseModel().created_at, f)
        sleep(1)
        obj2 = datetime.strftime(BaseModel().created_at, f)
        self.assertNotEqual(obj1, obj2)

    def test_updated_at_instanciation(self):
        f = "%Y-%m-%dT%H:%M:%S"
        obj = BaseModel()
        created = datetime.strftime(obj.created_at, f)
        updated = datetime.strftime(obj.created_at, f)
        self.assertEqual(created, updated)

    def test_instance_args(self):
        obj = BaseModel(name="kelvin", number=10)
        self.assertEqual(obj.name, "kelvin")
        self.assertEqual(obj.number, 10)

    def test_save(self):
        obj = BaseModel(name="kelvin")
        old = obj.updated_at
        obj.name = "morgan"
        obj.save()
        self.assertNotEqual(old, obj.updated_at)



if __name__ == "__main__":
    unittest.main()
