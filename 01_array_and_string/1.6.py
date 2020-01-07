import unittest


# Compress a string by replacing consecutive characters with a character and the number of the character.
# Return the original string if the length of the compressed string is longer than the original one.
def compress(string):
    if len(string) == 0:
        return string

    count = 1
    compressed = string[0]
    for i in range(1, len(string), 1):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed += str(count)
            compressed += string[i]
            count = 1
    compressed += str(count)

    if len(compressed) > len(string):
        return string
    return compressed


class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(compress("abcde"), "abcde")
        self.assertEqual(compress("aaaaabbcde"), "a5b2c1d1e1")
        self.assertEqual(compress("abbbcdee"), "abbbcdee")
        self.assertEqual(compress("abbbbbcdee"), "a1b5c1d1e2")


if __name__ == '__main__':
    unittest.main()