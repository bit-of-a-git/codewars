from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # First step is to reverse the rows, so the last is first and vice versa
        top = 0
        bottom = n - 1
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1
        # Now, items at matrix[0][2] should be at matrix[2][0], for example
        for i in range(n):
            # If i and j are the same, we don't need to switch
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
