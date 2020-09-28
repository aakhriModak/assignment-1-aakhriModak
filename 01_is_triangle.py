"""
Given three sides of a triangle, return True if it a triangle can be formed 
else return False.

Example 1
Input
side_1 = 1, side_2 = 2, side_3 = 3

Output
False

Example 2
Input
side_1 = 3, side_2 = 4, side_3 = 5

Output
True

Hint - Accordingly to Triangle inequality theorem, the sum of any two sides of
a triangle must be greater than measure of the third side

"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def is_triangle(side_1, side_2, side_3):
    # write your code here
     if side_1>0 and side_2>0 and side_3>0:
         if side_1+side_2>side_3 and side_2+side_3>side_1 and side_1+side_3>side_2:
             return True
         else:
             return False
     else:
          return False

    
        
# DO NOT TOUCH THE BELOW CODE


class TestIsTriangle(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_triangle(1, 2, 3), False)

    def test_02(self):
        self.assertEqual(is_triangle(2, 3, 1), False)

    def test_03(self):
        self.assertEqual(is_triangle(3, 1, 2), False)

    def test_04(self):
        self.assertEqual(is_triangle(3, 4, 5), True)

    def test_05(self):
        self.assertEqual(is_triangle(4, 5, 3), True)

    def test_06(self):
        self.assertEqual(is_triangle(5, 3, 4), True)

    def test_07(self):
        self.assertEqual(is_triangle(1, 2, 5), False)

    def test_08(self):
        self.assertEqual(is_triangle(2, 5, 1), False)

    def test_09(self):
        self.assertEqual(is_triangle(5, 1, 2), False)

    def test_10(self):
        self.assertEqual(is_triangle(0, 1, 1), False)

    def test_11(self):
        self.assertEqual(is_triangle(1, 0, 1), False)

    def test_12(self):
        self.assertEqual(is_triangle(1, 1, 0), False)

    def test_13(self):
        self.assertEqual(is_triangle(-1, 1, 2), False)

    def test_14(self):
        self.assertEqual(is_triangle(1, -1, 2), False)

    def test_15(self):
        self.assertEqual(is_triangle(1, 1, -2), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
