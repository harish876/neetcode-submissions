class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        1   2   3   3   4   5   6   7
                                    |

        {
            1:  0
            2:  0
            3:  0
            4:  0 X
            5:  1
            6:  1
            7:  1

        }

        0..groupSize

        [1,2,3,4] [2,3,4,5]
        

        

        n % groupSize == 0 

        groupSize: 4 -> increasing by 1

        """
        n = len(hand)
        if n % groupSize == 1:
            return False
        
        count = Counter(hand)
       
        while len(count):
            start = min(count.items(), key= lambda item: item[0])
            for i in range(groupSize):
                next_element = start[0] + i
                if (next_element) in count:
                    count[next_element] -= 1
                    if count[next_element] == 0:
                        del count[next_element]

                else:
                    return False

        return True