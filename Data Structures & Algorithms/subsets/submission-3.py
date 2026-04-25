class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            all possible subsets of nums

            [1,2,3] 

            either choose or not choose
        """

        result = []

        def dfs(idx: int, path: List[int]):
            if idx >= len(nums):
                result.append(path.copy())
                return
            
            dfs(idx+1,path)
            
            path.append(nums[idx])
            dfs(idx+1,path)
            path.pop()
            
        dfs(0,[])
        return result