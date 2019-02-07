import unittest


# Determine whether two strings has same permutations.
def same_permutations(string1, string2):
    if len(string1) != len(string2):
        return False
    
    letters = [0 for _ in range(128)]
    for c in string1:
        letters[ord(c)] += 1
    for c in string2:
        letters[ord(c)] -= 1
    
    for i in letters:
        if i != 0:
            return False
    return True


class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(same_permutations("abcde", "cbade"), True)
        self.assertEqual(same_permutations("abcde", "cbadf"), False)


if __name__ == '__main__':
    unittest.main()
