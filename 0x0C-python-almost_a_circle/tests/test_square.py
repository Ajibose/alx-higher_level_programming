#!/usr/bin/python3
"""Test for the Square class of `models/square.py'"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
from unittest.mock import patch
import io
from contextlib import redirect_stdout


class SquareInstatiationTest(unittest.TestCase):
    """Test the instantiation of the Square Class"""
    def test_square_rectangle_base(self):
        r = Square(1, 2, 3, 4)
        self.assertIsInstance(r, Base)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Square)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            r = Square()

    def test_one_arg(self):
        r = Square(2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.width, r.size)
        self.assertEqual(r.height, r.size)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertGreater(r.id, 0)

    def test_two_arg(self):
        r = Square(2, 3)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.width, r.size)
        self.assertEqual(r.height, r.size)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)
        self.assertGreater(r.id, 0)

    def test_three_arg(self):
        r = Square(2, 3, 4)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.width, r.size)
        self.assertEqual(r.height, r.size)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertGreater(r.id, 0)

    def test_four_args(self):
        r = Square(2, 3, 4, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_five_args(self):
        with self.assertRaises(TypeError):
            r = Square(2, 3, 4, 5, 6)

    def test_multiple_instances(self):
        r1 = Square(2, 3, 4)
        r2 = Square(2, 3, 4)
        self.assertNotEqual(r1.id, r2.id)
        r1 = Square(2, 3, 4, 5)
        r2 = Square(2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id)

    def test_id_none(self):
        r = Square(2, 3, 4, None)
        self.assertIsNotNone(r.id)
        self.assertGreater(r.id, 0)

    def test_id_string(self):
        r = Square(2, 3, 4, "string")
        self.assertIsNotNone(r.id)
        self.assertEqual(r.id, "string")

    def test_id_list(self):
        r = Square(2, 3, 4, [1, 2])
        self.assertIsNotNone(r.id)
        self.assertEqual(r.id, [1, 2])


class Square_sizeText(unittest.TestCase):
    """Test for Square width attribute"""
    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square((1, 2))

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square([1, 2])

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square("12")

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(float('inf'))

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(float('nan'))

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(0, 3)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square({"2": 3, "3": 4})

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(-1)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an intege"):
            r = Square(1.6)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(None)


class Square_xTest(unittest.TestCase):
    """Test for the Square x attribute"""
    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, (1, 2))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1, [1, 2])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(12, "2")

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(3, float('inf'))

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(3, float('nan'))

    def test_zero(self):
        self.assertEqual(Square(3, 0).x, 0)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(3, {"2": 3, "3": 4})

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Square(3, -3)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(3, 3.4)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(3, None)


class Square_yTest(unittest.TestCase):
    """Test for the Square y attribute"""
    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 5, (3, 4))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 5, [1, 2])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 5, "3")

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 3, float('inf'))

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 3, float('nan'))

    def test_zero(self):
        self.assertEqual(Square(3, 3, 0).y, 0)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 3, {"2": 3, "3": 4})

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Square(3, 4, -3)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(3, 3,  3.4)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(4, 3, None)
