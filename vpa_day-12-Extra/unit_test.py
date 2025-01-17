# Assert Methods in Python Unittest Framework

# unittest has lots of methods to assert on the values, types, and existence of variables. Below are some of the methods that are commonly used to write assertions.

# Method
	

# Description

# .assertEqual(a, b)
	
# Checks if a is equal to b, similar to the expression a == b.


# .assertTrue(x)

# Asserts that the boolean value of x is True, equivalent to bool(x) is True.


# .assertIsInstance(a, b)
	
# Asserts that a is an instance of class b, similar to the expression isinstance(a, b).


# .assertIsNone(x)	

# Ensures that x is None, similar to the expression x is None.


# .assertFalse(x)	

# Asserts that the boolean value of x is False, similar to bool(x) is False.


# .assertIs(a, b)	

# Verifies if a is identical to b, akin to the expression a is b.


# .assertIn(a, b)	

# Checks if a is a member of b, akin to the expression a in b.

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()
