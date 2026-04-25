class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            Combination Sum

            [2, 5, 6, 9]
            target = 9

            for loop
        """

        result = []

        def dfs(idx: int, target: int, path: List[int]):
            if target < 0 or idx >= len(nums):
                return
            
            if target == 0:
                result.append(path.copy())
                return
            

            path.append(nums[idx])
            dfs(idx, target-nums[idx], path)
            path.pop()


            dfs(idx+1, target, path)


        def dfs1(idx: int, target: int, path: List[int]):
            if target < 0 or idx >= len(nums):
                return
            
            if target == 0:
                result.append(path.copy())
                return
            
            for i in range(idx,len(nums)):
                if target - nums[i] < 0:
                    continue
                
                path.append(nums[i])
                dfs1(i, target - nums[i], path)
                path.pop()
            

        #dfs(0,target,[])
        dfs1(0,target,[])
        return result