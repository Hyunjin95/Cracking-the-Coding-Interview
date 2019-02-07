import unittest


# There is a method called is_substring() which determines whether a string A is a substring of the other string B.
# In the input strings s1 and s2, check if s2 is the result of rotating s1 by calling is_substring() once.
def is_rotated(s1, s2):
    doubled = s1 + s1
    # "".find() can be is_substring() of this problem.
    if doubled.find(s2) > -1:
        return True
    return False


class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(is_rotated("abc", "bca"), True)
        self.assertEqual(is_rotated("abc", "cba"), False)
        self.assertEqual(is_rotated("abc", "abd"), False)


if __name__ == '__main__':
    unittest.main()