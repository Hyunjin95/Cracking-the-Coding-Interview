import unittest

# If an element in an MxN matrix is 0, set all the elements of both a row and a column containing the number to 0.
# The limit of additional space is O(1)!
def zero_matrix(mat):
    if len(mat) == 0:
        return
    
    len_row, len_col = len(mat), len(mat[0])
    row_has_zero, col_has_zero = False, False
    
    for i in range(len_row):
        if mat[i][0] == 0:
            row_has_zero = True
            break
    
    for j in range(len_col):
        if mat[0][j] == 1:
            col_has_zero = True
            break
    
    for i in range(1, len_row, 1):
        for j in range(1, len_col, 1):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
    
    for i in range(len_row):
        if mat[i][0] == 0:
            for j in range(len_col):
                mat[i][j] = 0
    
    for j in range(len_col):
        if mat[0][j] == 0:
            for i in range(len_row):
                mat[i][j] = 0
    
    if row_has_zero:
        for i in range(len_row):
            mat[i][0] = 0
    
    if col_has_zero:
        for j in range(len_col):
            mat[0][j] = 0


class Test(unittest.TestCase):
    
    def test(self):
        test_mat = [
            [1, 2, 3, 0],
            [5, 0, 7, 8],
            [9, 10, 11, 12],
            [0, 14, 15, 16]
        ]
        expected = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 11, 0],
            [0, 0, 0, 0]
        ]
        zero_matrix(test_mat)
        self.assertEqual(test_mat, expected)


if __name__ == '__main__':
    unittest.main()