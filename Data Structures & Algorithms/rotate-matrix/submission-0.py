class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
            Rotate a matrix clockwise

            1   2
            3   4

            without doing in place its essentially column transpose
            lets first do that right
        """

        n = len(matrix)
        col, tmp = 0, [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(n):
                tmp[j][col] = matrix[i][j]
            col += 1
        
        print(tmp)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = tmp[i][j]
        

        



