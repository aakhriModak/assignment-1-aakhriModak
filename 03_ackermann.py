"""
Ackermann function is defined as  A(m, n)   = n + 1 if m = 0
                                            = A(m-1, 1) if m > 0 and n = 0
                                            = A(m-1, A(m, n-1)) if m > 0 and n > 0

Example 1

Input
m = 3 and n = 4

Output
125
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def ackermann(m, n):
   # write your code here

# DO NOT TOUCH THE BELOW CODE


class TestAckermann(unittest.TestCase):

    def test_01(self):
        self.assertEqual(ackermann(3, 4), 125)

    def test_02(self):
        self.assertEqual(ackermann(3, 3), 61)

    def test_03(self):
        self.assertEqual(ackermann(1, 0), 2)

    def test_04(self):
        self.assertEqual(ackermann(0, 1), 2)

    def test_05(self):
        self.assertEqual(ackermann(1, 1), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
