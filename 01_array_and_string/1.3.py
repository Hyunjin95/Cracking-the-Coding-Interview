import unittest


# Replace all blank spaces of a string by '%20'.
def urlify(string):
    return string.replace(" ", "%20")


class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(urlify("https://www. af.mil "), "https://www.%20af.mil%20")
        self.assertEqual(urlify("https://www.  af.mi l"), "https://www.%20%20af.mi%20l")
    

if __name__ == '__main__':
    unittest.main()