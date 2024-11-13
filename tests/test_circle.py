import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area(self):
        radius = 3
        result = area(radius)
        self.assertAlmostEqual(result, math.pi * radius * radius)

    def test_perimeter(self):
        radius = 3
        result = perimeter(radius)
        self.assertAlmostEqual(result, 2 * math.pi * radius)

    def test_area_negative(self):
        radius = -3
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_negative(self):
        radius = -3
        with self.assertRaises(ValueError):
            perimeter(radius)


if __name__ == '__main__':
    unittest.main()
