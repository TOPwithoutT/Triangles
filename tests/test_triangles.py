import unittest
import io
from contextlib import redirect_stdout
from unittest.mock import patch

from triangles import classify_triangle, main, _to_number

class TestTriangles(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_3_4_5(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Right")

    def test_right_float(self):
        self.assertEqual(classify_triangle(1.5, 2.0, 2.5), "Right")

    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classify_triangle(2, 3, 5), "NotATriangle")

    def test_invalid_zero_or_negative(self):
        self.assertEqual(classify_triangle(0, 1, 1), "InvalidInput")
        self.assertEqual(classify_triangle(-1, 2, 2), "InvalidInput")

    def test_invalid_types(self):
        self.assertEqual(classify_triangle("3", 3, 3), "InvalidInput")
        self.assertEqual(classify_triangle(True, 3, 3), "InvalidInput")

    def test__to_number(self):
        self.assertIsNone(_to_number("true"))
        self.assertIsNone(_to_number("false"))
        self.assertEqual(_to_number("3.5"), 3.5)
        self.assertIsNone(_to_number("abc"))

    def test_cli_args_right(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main(["3", "4", "5"])
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "Right")

    def test_cli_args_invalidinput(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main(["true", "3", "3"])  # "true" should be InvalidInput
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "InvalidInput")

    def test_cli_args_wrong_count(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main(["3", "4"]) 
        self.assertEqual(rc, 2)


    @patch("builtins.input", side_effect=["3", "3", "3"])
    def test_cli_interactive_equilateral(self, _):
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = main([])  
        self.assertEqual(rc, 0)
        self.assertEqual(buf.getvalue().strip(), "Equilateral")
