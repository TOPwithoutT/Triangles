import unittest
from triangles import classify_triangle

class TestTriangles(unittest.TestCase):
    # ----- Valid classifications -----
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

    # ----- Not a triangle (fails triangle inequality) -----
    def test_not_a_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classify_triangle(2, 3, 5), "NotATriangle")

    # ----- Invalid inputs -----
    def test_invalid_zero_or_negative(self):
        self.assertEqual(classify_triangle(0, 1, 1), "InvalidInput")
        self.assertEqual(classify_triangle(-1, 2, 2), "InvalidInput")

    def test_invalid_types(self):
        self.assertEqual(classify_triangle("3", 3, 3), "InvalidInput")
        self.assertEqual(classify_triangle(True, 3, 3), "InvalidInput")  # bool is invalid

if __name__ == "__main__":
    unittest.main()
