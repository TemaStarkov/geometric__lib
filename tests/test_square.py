import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area(self):
        side = 4
        result = area(side)
        self.assertEqual(result, 16)

    def test_perimeter(self):
        side = 4
        result = perimeter(side)
        self.assertEqual(result, 16)

    def test_area_negative(self):
        side = -4
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_negative(self):
        side = -4
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == '__main__':
    unittest.main()
