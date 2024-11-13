import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area(self):
        a, b, c = 3, 4, 5
        result = area(a, b, c)
        self.assertAlmostEqual(result, 6.0)

    def test_perimeter(self):
        a, b, c = 3, 4, 5
        result = perimeter(a, b, c)
        self.assertEqual(result, 12)

    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)


if __name__ == '__main__':
    unittest.main()
