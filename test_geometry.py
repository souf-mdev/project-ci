import unittest
from geometry import rectangle_area, rectangle_perimeter, circle_area , circle_circumference

class TestGeometry(unittest.TestCase):
    
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(6, 3), 18)

    def test_circle_area(self):
        self.assertEqual(circle_area(8), 200.96 )

    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(9), 28.26 )

if __name__ == '__main__':
    unittest.main()
