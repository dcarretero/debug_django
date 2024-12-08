from django.test import TestCase

# Create your tests here.

class TestMath(TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(1 - 1, 0)

    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)

    def test_division(self):
        self.assertEqual(6 / 2, 3)

