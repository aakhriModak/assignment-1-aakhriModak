"""
Given two points on a 2-D plane, return the distance between the two points. 

Assumption - Retain only the integer

Example 1

Input
point_1 = (1, 2) and point_2 = (3, 2)

Output
2

Example 2

Input
point_1 = (1, 4) and point_2 = (2, 5)

Output
4

Explaination - The actual distance is around 4.2426....  
Only consider the integer part 4
"""


import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def distance(point_1, point_2):
    # write your code here
    v=((point_1[0]-point_2[0])**2)+((point_1[1]-point_2[1])**2)
    y=int(v**0.5)
    return y
# DO NOT TOUCH THE BELOW CODE


class TestDistance(unittest.TestCase):

    def test_01(self):
        point_1 = (1,2)
        point_2 = (3, 2)
        self.assertEqual(distance(point_1, point_2), 2)

    def test_02(self):
        point_1 = (-1,2)
        point_2 = (3,2)
        self.assertEqual(distance(point_1, point_2), 4)

    def test_03(self):
        point_1 = (-1, 2)
        point_2 = (-3, 2)
        self.assertEqual(distance(point_1, point_2), 2)

    def test_04(self):
        point_1 = (1, 2)
        point_2 = (1, 2)
        self.assertEqual(distance(point_1, point_2), 0)

    def test_05(self):
        point_1 = (1, 2)
        point_2 = (4, 5)
        self.assertEqual(distance(point_1, point_2), 4)

    def test_06(self):
        point_1 = (1, 2)
        point_2 = (3, 4)
        self.assertEqual(distance(point_1, point_2), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
