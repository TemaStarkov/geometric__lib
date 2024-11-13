import unittest
from calculate import calc
from square import area as square_area, perimeter as square_perimeter
from circle import area as circle_area, perimeter as circle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCalculations(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square_area(4), 16)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.84955592153876)

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_calc_square_area(self):
        self.assertEqual(calc('square', 'area', [4]), 16)

    def test_calc_square_perimeter(self):
        self.assertEqual(calc('square', 'perimeter', [4]), 16)

    def test_calc_circle_area(self):
        self.assertAlmostEqual(calc('circle', 'area', [3]), 28.274333882308138)

    def test_calc_circle_perimeter(self):
        self.assertAlmostEqual(calc('circle', 'perimeter', [3]), 18.84955592153876)

    def test_calc_triangle_area(self):
        self.assertAlmostEqual(calc('triangle', 'area', [3, 4, 5]), 6.0)

    def test_calc_triangle_perimeter(self):
        self.assertEqual(calc('triangle', 'perimeter', [3, 4, 5]), 12)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc('hexagon', 'area', [3, 4, 5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc('square', 'volume', [4])


if __name__ == '__main__':
    unittest.main()
