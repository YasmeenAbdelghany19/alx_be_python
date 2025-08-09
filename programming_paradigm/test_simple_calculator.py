"""Create a test_simple_calculator.py script to define and run unit tests for each method in the SimpleCalculator class. Your tests should cover various scenarios to ensure the class functions correctly.

Guidelines for Writing Tests:
Import the Necessary Modules:

Import the unittest module and the SimpleCalculator class from simple_calculator.py.
Define a Test Class:

Create a test class that inherits from unittest.TestCase.
Write Test Methods:

Write at least one test method for each operation (add, subtract, multiply, divide) provided by the SimpleCalculator.
Include tests for edge cases, such as dividing by zero.
Use Assertions to Verify Results:

Utilize self.assertEqual() to check for expected outcomes.
For the divide method, ensure you test both normal operation and division by zero.
Running Your Tests:

Run your tests using the command line: python -m unittest test_simple_calculator.py."""

import unittest
from programming_paradigm.simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 3), 2/3)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(1, 0), None)

if __name__ == "__main__":
    unittest.main()
