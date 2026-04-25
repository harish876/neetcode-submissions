class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
            [
                0   -   [2,5,6]
                1   -   [1,4,4]
                2   -   [5,7,5]
                target - [5,4,6]

                merge everything


                [[2,6,6],[10,5,1],[8,9,2],[7,2,9],[5,10,6]]
                
                2,6,6
                [10,6,6]

                ignore triplets where the value might be greater than the largest value in the final target


            ]
        """
        max_target = max(target)
        n, final_triplet = len(triplets), [0,0,0]

        for i in range(n):
            if max(triplets[i]) > max_target:
                continue

            final_triplet = [max(final_triplet[j], triplets[i][j]) for j in range(3)]
            if final_triplet == target:
                return True
        
        return False

