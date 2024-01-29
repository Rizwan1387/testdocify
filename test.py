import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Test cases for the Calculator class
class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test case
        print("Setting up test...")

    def tearDown(self):
        # This method will be called after each test case
        print("Tearing down test...")

    def test_add(self):
        # Test the add method of the Calculator class
        calculator = Calculator()
        result = calculator.add(3, 5)
        self.assertEqual(result, 8)  # Assert that the result is equal to 8

    def test_subtract(self):
        # Test the subtract method of the Calculator class
        calculator = Calculator()
        result = calculator.subtract(10, 4)
        self.assertEqual(result, 6)  # Assert that the result is equal to 6

if __name__ == '__main__':
    unittest.main()
