class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int left = 0;
        int right = n-1;
        /*
            1   7   2   5   4   7   3   6
        l       |
        r                               |

            if 1 < 6 then move right
            if 7 > 6 then 
        */
        int area = 0;
        while(left < right){
            int currArea = min(heights[left],heights[right]) * (right - left);
            area = max(area,currArea);
            if(heights[left] < heights[right]){
                left++;
            }
            else{
                right--;
            }

        }
        return area;
    }
};
