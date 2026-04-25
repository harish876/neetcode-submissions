class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            2   1   5   6   2   3
                        
                        |
                    |   |
                    |   |
                    |   |       |
            |       |   |   |   |
            |   |   |   |   |   |

            0   1   2   3   4   5
                            |



            7   1   7   2   2   4




            (1,1)
            
            (7,0)


            (6,3)
            (5,2)
            (1,0)


            area = 3 * (6-5) = 3
            area = 2 * (6-2) = 8
            area = 1 * 6 = 6

            2 * 3 = 6

        """


        curr, n, stack = 0,len(heights) ,[]
        result = 0

        while curr < n:
            insert_idx = curr
            while len(stack) and stack[-1][0] > heights[curr]:
                height, start = stack.pop()
                result = max(result, height * (curr - start))
                insert_idx = start
            
            stack.append((heights[curr],insert_idx))
            curr += 1
        
        while len(stack):
            result = max(result, stack[-1][0] * (n - stack[-1][1]))
            stack.pop()
        
        return result


