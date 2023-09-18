#!/usr/bin/python3
"""Unittest for the Base class of module `models/base.py`"""


import unittest
from models.base import Base


class BaseInstantiationTest(unittest.TestCase):
    """Test the Initailization of Base class"""
    def test_no_arg(self):
        self.assertGreater(Base().id, 0)

    def test_multiple_base(self):
        b1 = Base()
        b2 = Base()
        self.assertGreater(b1.id, 0)
        self.assertGreater(b2.id, 0)
        self.assertNotEqual(b1.id, b2.id)

    def test_id_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertGreater(b1.id, 0)
        self.assertGreater(b2.id, 0)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_infinite(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_id_Nan(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_id_0(self):
        self.assertEqual(Base(0).id, 0)

    def test_id_sequence(self):
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base((1, 2, 3)).id, (1, 2, 3))
        self.assertEqual(Base("test").id, "test")

    def test_id_public(self):
        self.assertEqual(Base(24).id, 24)

    def test_private_nbinstance(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)
