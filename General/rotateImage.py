"""
Desc: given an n x n 2D matrix representing an image, rotate the image by 90 degrees clockwise. Do in place and do not allocate another 2D matrix for rotation
"""

def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)): 
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
