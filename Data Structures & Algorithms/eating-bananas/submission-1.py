class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            h = hours to eat all bananas

            k = number of bananas per hour

            h = 9

            k = 2
            h = 6
            
            [0,0,0,0]

            [1,4,3,2]

            k = 5
            1 // 5 + 1 % 5 = 1
            4 // 5 + 4 % 5 = 4
            3 // 2 + 3%2 = 2
            2 // 2 + 0 = 1 

        """

        def numHours(k: int) -> int:
            hours = 0
            
            for pile in piles:
                hours += (pile // k)

                if pile % k:
                    hours += 1
            
            return hours
        

        left, right, result = 1, sum(piles), 1

        """
            1 + 10 = 11 / 2 = 5
        """

        while left <= right:
            k = left + (right - left) // 2
            num_hours = numHours(k)

            if num_hours <= h:
                result = k
                right = k - 1
            
            else:
                left = k + 1
        
        return result

