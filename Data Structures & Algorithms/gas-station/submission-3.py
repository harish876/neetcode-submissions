class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            idx:    0   1   2   3   4
            reload: 1   2   3   4   5   
            cost:   3   4   5   1   2
                                |

            start =  3 + (1 - 2) = 2 + (2-2) = 2 + (3-4) = 1

            single pass??

        """
        total_reload = sum(gas)
        total_spend = sum(cost)

        if total_spend > total_reload:
            return -1
        
        curr_tank, n,  ans = 0, len(gas), 0
        for i in range(n):
            curr_tank += (gas[i] - cost[i])

            if curr_tank < 0:
                ans = i+1
                curr_tank = 0

        return ans