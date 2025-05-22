import unittest
from course_package.calculator import IntCalculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(IntCalculator("1 + 1").run(), 2)

    def test_sub(self):
        self.assertEqual(IntCalculator("1 - 1").run(), 0)

    def test_div(self):
        self.assertEqual(IntCalculator("4 / 2").run(), 2)

    def test_multi(self):
        self.assertEqual(IntCalculator("2 * 2").run(), 4)


if __name__ == "__main__":
    unittest.main()
