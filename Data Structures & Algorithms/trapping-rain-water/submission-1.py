class Solution:
    def trap(self, height: List[int]) -> int:
        """             
                        |               |
                |       |               |   |
            _   |   _   |   |   _   |   |   |   |
           -1   0   0   0   0   0   0   0   0   0
        L   0   0   0   0   0   0   0   0   0   0
        R                7   
           
        
        """
        n = len(height)
        result = 0
        # would consist of indices i believe
        greatest_left_idx = [-1] * n
        greatest_right_idx = [-1] * n

        max_left = height[0]
        max_left_idx = -1

        for i in range(n):
            if height[i] >= max_left:
                max_left = height[i]
                max_left_idx = i
            
            greatest_left_idx[i] = max_left_idx

        max_right = height[n-1]
        max_right_idx = -1

        for i in range(n-1,-1,-1):
            if height[i] >= max_right:
                max_right = height[i]
                max_right_idx = i
            
            greatest_right_idx[i] = max_right_idx

        for i in range(n):
            if greatest_left_idx[i] != -1 and greatest_right_idx[i] != -1:
                result += min(height[greatest_right_idx[i]], height[greatest_left_idx[i]]) - height[i] 

        return result