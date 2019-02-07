import unittest


# 1.1 - Check if a string has duplicate characters.
def has_duplicate(string):
    if len(string) > 128:
        return True
    
    letters = [False for _ in range(128)]
    for c in string:
        val = ord(c)
        if letters[val]:
            return True
        letters[val] =True
    
    return False 


class Test(unittest.TestCase):

    def test(self):
        unique = "abcdefghijklmnopqrstuvwxyz"
        dup = "abcdefghijklmanopqrstuvwxyz"
        self.assertEqual(has_duplicate(unique), False)
        self.assertEqual(has_duplicate(dup), True)


if __name__ == '__main__':
    unittest.main()