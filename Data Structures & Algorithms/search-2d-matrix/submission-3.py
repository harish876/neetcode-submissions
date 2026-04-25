class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            [
                1  2   4   8
                10  [11]  12  13
                14  20  30  40
            ]
        """

        m,n = len(matrix),len(matrix[0])
        curr_row = 0
        left_col, right_col = 0, n

        while curr_row < m and left_col < right_col:
            
            mid = left_col + (right_col - left_col) // 2
                
            if matrix[curr_row][mid] == target:
                return True

            elif target > matrix[curr_row][right_col-1]:
                curr_row += 1
            
            elif target > matrix[curr_row][mid]:
                left_col = mid+1
                
            else:
                right_col = mid
                    
        return False




