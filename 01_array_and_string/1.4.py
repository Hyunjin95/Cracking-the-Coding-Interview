import unittest


# Determine whether a string has a palindrome permutation.
def has_palindrome_permutation(string):
    letters = [0 for _ in range(128)]
    odd_numbers = 0
    
    for c in string.replace(" ", ""):
        letters[ord(c)] += 1
    for i in letters:
        if i % 2 == 1:
            odd_numbers += 1
            if odd_numbers > 1:
                return False

    return True


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(has_palindrome_permutation("abcba"), True)
        self.assertEqual(has_palindrome_permutation("abcbd"), False)
        self.assertEqual(has_palindrome_permutation("abccba"), True)
        self.assertEqual(has_palindrome_permutation("abccda"), False)


if __name__ == '__main__':
    unittest.main()