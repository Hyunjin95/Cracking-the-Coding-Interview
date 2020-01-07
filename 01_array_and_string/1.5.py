import unittest


# Check if two strings can be the same by less than one modification.
# The modification includes inserting, deleting, replacing a character.
def modify_once(string1, string2):
    len_string1 = len(string1)
    len_string2 = len(string2)

    if len_string1 == len_string2 - 1:
        return edit_string(string1, string2)
    elif len_string1 == len_string2 + 1:
        return edit_string(string2, string1)
    elif len_string1 == len_string2:
        diff_count = 0
        for i in range(len_string1):
            if string1[i] != string2[i]:
                if diff_count > 0:
                    return False
                diff_count += 1
        return True
    return False


def edit_string(shorter, longer):
    index1, index2 = 0, 0
    while index1 < len(shorter) and index2 < len(shorter):
        if shorter[index1] != longer[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


class Test(unittest.TestCase):
    
    def test(self):
        self.assertEqual(modify_once("abc", "abd"), True)
        self.assertEqual(modify_once("abc", "ab"), True)
        self.assertEqual(modify_once("abc", "ac"), True)
        self.assertEqual(modify_once("abc", "abe"), True)
        self.assertEqual(modify_once("abc", "ade"), False)


if __name__ == '__main__':
    unittest.main()