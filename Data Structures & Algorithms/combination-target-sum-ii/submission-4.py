class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            [9, 2, 2, 4, 6, 1, 5]

            target = 8

            no duplicates

            1,2,2,4,5,6,9

            1
        """

        result, n = [], len(candidates)
        candidates.sort()
        print(candidates)

        def dfs(idx:int, target: int, path: List[int]):
            if target == 0:
                result.append(path.copy())
                return
            
            if target < 0 or idx >= n:
                return
                        
            for i in range(idx,n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                dfs(i+1,target - candidates[i],path)
                path.pop()

        
        dfs(0,target,[])
        return result
