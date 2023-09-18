#!/usr/bin/python3
"""Test for the Rectangle class of `models/rectangle.py'"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io
from contextlib import redirect_stdout


class RectangleInstatiationTest(unittest.TestCase):
    """Test the instantiation of the Rectangle Class"""
    def test_rectangle_base(self):
        self.assertIsInstance(Rectangle(1, 2, 3, 4, 5), Base)
        self.assertIsInstance(Rectangle(1, 2, 3, 4, 5), Rectangle)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2)

    def test_two_arg(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertGreater(r.id, 0)

    def test_three_arg(self):
        r = Rectangle(2, 3, 4)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 0)
        self.assertGreater(r.id, 0)

    def test_four_args(self):
        r = Rectangle(2, 3, 4, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        self.assertGreater(r.id, 0)

    def test_five_args(self):
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 6)

    def test_six_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 4, 5, 6, 7)

    def test_multiple_instances(self):
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(2, 3, 4, 5)
        self.assertNotEqual(r1.id, r2.id)

    def test_id_none(self):
        r = Rectangle(2, 3, 4, 5, None)
        self.assertIsNotNone(r.id)
        self.assertGreater(r.id, 0)


class Rectangle_widthText(unittest.TestCase):
    """Test for Rectangle width attribute"""

    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1, 2), 2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([1, 2], 2)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("12", 2)

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(float('inf'), 3)

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(float('nan'), 3)

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 3)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({"2": 3, "3": 4}, 5)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 3)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(1.3, 3)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 3)


class Rectangle_heightTest(unittest.TestCase):
    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (1, 2))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [1, 2])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(12, "2")

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, float('inf'))

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, float('nan'))

    def test_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(3, 0)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(5, {"2": 3, "3": 4})

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(3, -3)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, 3.4)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, None)


class Rectangle_xText(unittest.TestCase):
    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 3, (1, 2))

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 3, [1, 2])

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(12, 3, "2")

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 3, float('inf'))

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 3, float('nan'))

    def test_zero(self):
        self.assertEqual(Rectangle(3, 3, 0).x, 0)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(5, 3, {"2": 3, "3": 4})

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(3, 4, -3)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 3, 3.4)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 3, None)


class Rectangle_yTest(unittest.TestCase):
    def test_sequence(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 3, 2, (1, 2))

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 3, 2, [1, 2])

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(12, 3, 3, "2")

    def test_infinite(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(3, 3, 5, float('inf'))

    def test_Nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(3, 3, 2, float('nan'))

    def test_zero(self):
        self.assertEqual(Rectangle(3, 3, 2, 0).y, 0)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(5, 3, 8, {"2": 3, "3": 4})

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(3, 4, 1, -3)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(3, 3, 2, 3.4)

    def test_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 3, 4, None)


class Rectangle_AreaTest(unittest.TestCase):
    def test_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2).area(3)

    def test_small(self):
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_large(self):
        r = Rectangle(4678932898309202933989, 463789208732902899378)
        self.assertEqual(r.area(), 2170038586621173255031958254972722443158842)


class Rectangle_DisplayTest(unittest.TestCase):
    def test_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2).display(3)

    def test_small(self):
        s = "#\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            Rectangle(1, 1).display()
            actual_output = mock_stdout.getvalue()

        self.assertEqual(s, actual_output)

    def test_large(self):
        s = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n"

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            Rectangle(4, 5, 2, 2).display()
            actual_output = mock_stdout.getvalue()

        self.assertEqual(s, actual_output)


class Rectangle_strTest(unittest.TestCase):
    """Test the str method of Rectangle"""
    def test_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 2).__str__(53)

    def test_with_print(self):
        self.assertEqual(
                Rectangle(4, 6, 2, 1, 12).__str__(),
                "[Rectangle] (12) 2/1 - 4/6")

        # missing id
        r = Rectangle(4, 6, 2, 1)
        self.assertEqual(
                str(r), f"[Rectangle] ({r.id}) 2/1 - 4/6")

        # missing y
        r = Rectangle(4, 6, 2)
        s = f"[Rectangle] ({r.id}) 2/0 - 4/6"
        self.assertEqual(str(r), s.format(r.id))

        # missing x
        r = Rectangle(4, 6)
        self.assertEqual(str(r), f"[Rectangle] ({r.id}) 0/0 - 4/6")

        # missing height
        with self.assertRaises(TypeError):
            r = Rectangle(4)
            self.assertEqual(str(r), f"[Rectangle] ({r.id}) 0/0 - 4/6")

        # missing width
        with self.assertRaises(TypeError):
            r = Rectangle()
            self.assertEqual(str(r), f"[Rectangle] ({r.id}) 0/0 - 4/6")


class Rectangle_UpdateTest_args(unittest.TestCase):
    """Test the update method of class Rectangle"""
    def setUp(self):
        self.r1 = Rectangle(10, 10, 10, 10)

    def test_no_arg(self):
        s = "[Rectangle] ({}) 10/10 - 10/10"
        (self.r1).update()
        self.assertEqual(str(self.r1), s.format((self.r1).id))

    def test_one_arg(self):
        s = "[Rectangle] (89) 10/10 - 10/10"
        (self.r1).update(89)
        self.assertEqual(str(self.r1), s)

    def test_two_arg(self):
        s = "[Rectangle] (89) 10/10 - 4/10"
        (self.r1).update(89, 4)
        self.assertEqual(str(self.r1), s)

    def test_three_arg(self):
        s = "[Rectangle] (89) 10/10 - 4/1"
        (self.r1).update(89, 4, 1)
        self.assertEqual(str(self.r1), s)

    def test_four_arg(self):
        s = "[Rectangle] (89) 9/10 - 4/1"
        (self.r1).update(89, 4, 1, 9)
        self.assertEqual(str(self.r1), s)

    def test_five_arg(self):
        s = "[Rectangle] (89) 9/5 - 4/1"
        (self.r1).update(89, 4, 1, 9, 5)
        self.assertEqual(str(self.r1), s)

    def test_six_arg(self):
        s = "[Rectangle] (89) 9/5 - 4/1"
        (self.r1).update(89, 4, 1, 9, 5, 6)
        self.assertEqual(str(self.r1), s)

    def test_arg_zero(self):
        s = "[Rectangle] (0) 9/5 - 4/1"
        (self.r1).update(0, 4, 1, 9, 5, 6)
        self.assertEqual(str(self.r1), s)

        # width is zero
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            (self.r1).update(89, 0, 1, 9, 5)

        # Update height to zero
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            (self.r1).update(89, 3, 0, 9, 5)

        # Update x to zero
        s = "[Rectangle] (89) 0/5 - 4/1"
        (self.r1).update(89, 4, 1, 0, 5)
        self.assertEqual(str(self.r1), s)

        # Update y to zero
        s = "[Rectangle] (89) 8/0 - 4/1"
        (self.r1).update(89, 4, 1, 8, 0)
        self.assertEqual(str(self.r1), s)

    def test_update_negative(self):
        s = "[Rectangle] (-1) 9/5 - 4/1"
        (self.r1).update(-1, 4, 1, 9, 5, 6)
        self.assertEqual(str(self.r1), s)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            (self.r1).update(89, -1, 1, 9, 5)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            (self.r1).update(89, 3, -1, 9, 5)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            (self.r1).update(89, 4, 1, -1, 5)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            (self.r1).update(89, 4, 1, 6, -5)

    def test_update_noninteger(self):
        s = "[Rectangle] (1) 9/5 - 4/1"
        (self.r1).update("1", 4, 1, 9, 5, 6)
        self.assertEqual(str(self.r1), s)

        # Test width for negativity
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            (self.r1).update(89, "1", 1, 9, 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            (self.r1).update(89, None, 1, 9, 5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            (self.r1).update(89, 1.3, 1, 9, 5)

        # Test height for negativity
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            (self.r1).update(89, 2, "1", 9, 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            (self.r1).update(89, 2, None, 9, 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            (self.r1).update(89, 1, 1.4, 9, 5)

        # Test x for negativity
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            (self.r1).update(89, 2, 1, "9", 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            (self.r1).update(89, 2, 5, None, 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            (self.r1).update(89, 1, 1, 9.3, 5)

        # Test y for negativity
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            (self.r1).update(89, 2, 1, 9, "5")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            (self.r1).update(89, 2, 5, 5, None)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            (self.r1).update(89, 1, 1, 9, 5.1)


class Rectangle_UpdateTest_kwargs(unittest.TestCase):
    """Test for Rectangle kwargs update """
    def setUp(self):
        self.r = Rectangle(1, 1, 1, 1, 1)

    def test_update_zero(self):
        self.r.update()
        self.assertEqual("[Rectangle] (1) 1/1 - 1/1", str(self.r))

    def test_update_dict(self):
        self.r.update({})
        self.assertEqual("[Rectangle] ({}) 1/1 - 1/1", str(self.r))

    def test_update_one(self):
        self.r.update(id=11)
        self.assertEqual("[Rectangle] (11) 1/1 - 1/1", str(self.r))

    def test_update_two(self):
        self.r.update(id=11, width=12)
        self.assertEqual("[Rectangle] (11) 1/1 - 12/1", str(self.r))

    def test_update_three(self):
        self.r.update(id=11, width=12, height=13)
        self.assertEqual("[Rectangle] (11) 1/1 - 12/13", str(self.r))

    def test_update_four(self):
        self.r.update(id=11, width=12, height=13, x=14)
        self.assertEqual("[Rectangle] (11) 14/1 - 12/13", str(self.r))

    def test_update_four(self):
        self.r.update(id=11, width=12, height=13, x=14, y=15)
        self.assertEqual("[Rectangle] (11) 14/15 - 12/13", str(self.r))

    def test_notan_attribute(self):
        self.r.update(id=11, width=12, height=13, x=14, y=15, z=16)
        self.assertEqual("[Rectangle] (11) 14/15 - 12/13", str(self.r))

    def test_mixed_args_kwargs(self):
        self.r.update(11, 12, height=13, x=14, y=15)
        self.assertEqual("[Rectangle] (11) 1/1 - 12/1", str(self.r))

        self.r.update(11, 12, width=13, x=14, y=15)
        self.assertEqual("[Rectangle] (11) 1/1 - 12/1", str(self.r))
