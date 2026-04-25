class Solution:
    def condition(self,piles: List[int],k: int ,h: int) -> bool:
        score = 0
        for pile in piles:
            score += math.ceil(pile / k)
        
        return score <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            eating rate is k

            all bananas within h hours

            [1,4,3,2]
            h = 9

            k = 2
            h = 0

            for pile in piles:
                h += ceil(pile / k)

            h = 1 [1,4,3,2]
            1 - 1
            4 - 2
            3 - 2
            2 - 

            while left <= right:
                mid = left + (right-left)//2

                if condition(piles,mid,h):
                    right = mid
                
                else:
                    left = mid + 1

            return right

            [25,10,23,4]

        """
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right-left)//2

            if self.condition(piles,mid,h):
                right = mid
                
            else:
                left = mid + 1

        return right
