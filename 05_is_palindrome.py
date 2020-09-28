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


def is_palindrome(s_1, s_2):
    # write your code here
    if s_1.equals(s_2):
        if s_1.reverse()==s_2
            return True
        else:
            return False


# DO NOT TOUCH THE BELOW CODE


class TestIsPalindrome(unittest.TestCase):

    def test_01(self):
        string_1 = "madam"
        string_2 = "madam"
        self.assertEqual(is_palindrome(string_1, string_2), True)

    def test_02(self):
        string_1 = "madam"
        string_2 = "Madam"
        self.assertEqual(is_palindrome(string_1, string_2), False)

    def test_03(self):
        string_1 = "first"
        string_2 = "fist"
        self.assertEqual(is_palindrome(string_1, string_2), False)

    def test_04(self):
        string_1 = "first"
        string_2 = "fist"
        self.assertEqual(is_palindrome(string_1, string_2), False)

    def test_05(self):
        string_1 = "peep"
        string_2 = "keep"
        self.assertEqual(is_palindrome(string_1, string_2), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
