"""
Fibonacci series is defined as  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... 
Find out whether a given number is fibonacci number or not

Example 1

Input
n = 8

Output
True


Example 2

Input
n = 7

Output
False

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def is_fibonacci(n):
    #write your code here

# DO NOT TOUCH THE BELOW CODE


class TestIsFibonacci(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_fibonacci(8), True)

    def test_02(self):
        self.assertEqual(is_fibonacci(7), False)

    def test_03(self):
        self.assertEqual(is_fibonacci(0), True)

    def test_04(self):
        self.assertEqual(is_fibonacci(1), True)

    def test_05(self):
        self.assertEqual(is_fibonacci(1597), True)

    def test_06(self):
        self.assertEqual(is_fibonacci(1134903170), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
