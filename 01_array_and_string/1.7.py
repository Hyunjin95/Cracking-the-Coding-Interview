import unittest


# In a NxN matrix representing an image, rotate the matrix to 90 degrees to the right side.
# Each pixel of the matrix consists of four bytes and the limit of additional space is O(n).
def rotate_matrix(mat):
    len_mat = len(mat)
    layer = 0

    while layer * 2 < len_mat:
        first, last = 0+layer, len_mat-layer-1
        for i in range(first, last, 1):
            offset = i - first
            tmp_top = mat[first][i]
            # left -> top
            mat[first][i] = mat[last-offset][first]
            # bottom -> left
            mat[last-offset][first] = mat[last][last-offset]
            # right -> bottom
            mat[last][last-offset] = mat[i][last]
            # top -> right
            mat[i][last] = tmp_top
        layer += 1


class Test(unittest.TestCase):
    
    def test(self):
        test_mat = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        
        rotate_matrix(test_mat)
        self.assertEqual(test_mat, expected)


if __name__ == '__main__':
    unittest.main()