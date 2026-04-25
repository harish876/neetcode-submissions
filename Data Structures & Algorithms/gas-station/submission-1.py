class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            idx - 0   1   2   3   
            gas - 1   2   3   4
            cost- 2   2   4   1

            idx = 3
            curr = 4 + 1 - ()


            O(n) vs O(n^2) 

            lets do brute force first right, simplest way
        """

        n = len(gas)
        
        
        def isValid(idx:int) -> bool:
            curr = 0
            
            for i in range(idx,n):
                curr += gas[i]
                curr -= cost[i]

                if curr < 0:
                    return False
            
            for i in range(idx):
                curr += gas[i]
                curr -= cost[i]

                if curr < 0:
                    return False
            
            return True

        
        for idx in range(n):
            if isValid(idx):
                return idx
        
        return -1


