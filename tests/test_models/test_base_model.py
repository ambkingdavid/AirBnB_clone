#!/usr/bin/env python3

import os
import sys
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel_instance(unittest.TestCase):
	def test_instance(self):
		self.assertIsInstance(BaseModel(), BaseModel)

	def test_instance_attribute_id(self):
		self.assertIsInstance(BaseModel().id, str)

	def test_instance_attribute_created_at(self):
		f = "%Y-%m-%dT%H:%M"
		self.assertEqual(datetime.strftime(datetime.today(), f),
				datetime.strftime(BaseModel().created_at, f))
	def test_instance_attribute_kwargs(self):
		k = BaseModel(name="kelvin", number=10)
		self.assertEqual(k.name, "kelvin")
		self.assertEqual(k.number, 10)

	def test_instance_string_rep(self):
		k = BaseModel()
		fs = "[{}] ({}) {}".format("BaseModel", k.id, k.__dict__)
		self.assertEqual(f"{k}", fs)  

class TestBaseModel_save(unittest.Testcase)
	def test_save_json(self):




if __name__ == "__main__":
	unittest.main()
