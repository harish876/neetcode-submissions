class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            0   1   2   3
            |           |
                |
            1   2   4   8
            10  11  12  13
            14  20  30  40

            find 10
        """
        
        left = 0
        right = len(matrix[0])-1
        row = 0

        while row < len(matrix) and (left <= right):
            mid = left + (right-left)//2
            key = matrix[row][mid]
            rightKey = matrix[row][right]

            if target > rightKey:
                row = row + 1

            elif key == target:
                return True
            
            elif target > key:
                left = mid+1
            
            else:
                right = mid-1

        return False