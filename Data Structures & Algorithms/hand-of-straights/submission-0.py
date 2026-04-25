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
                if (start[0] + i) in count:
                    count[i + start[0]] -= 1
                    if count[i + start[0]] == 0:
                        del count[i + start[0]]

                else:
                    return False


        return True