class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            [1,2,1]

            i can sort it and still get the subsets? No.

            [1,1,2]

            []

        """

        result, n = [], len(nums)
        nums.sort()
        
        def dfs(idx: int, path: List[int]):
            if idx > n:
                return
            
            result.append(path.copy())

            for i in range(idx,n):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                dfs(i+1,path)
                path.pop()

        dfs(0,[])
        return result

