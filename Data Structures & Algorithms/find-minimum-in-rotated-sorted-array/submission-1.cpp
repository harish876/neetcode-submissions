class Solution {
public:
    int findMin(vector<int> &nums) {
        /*
            3   4   5   6   1   2
                    |

        */

        int n = nums.size();
        int left=0, right=n-1;

        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[right] >= nums[mid]){
                if(nums[right] >= nums[left]){
                    right--;
                }
                else{
                    left++;
                }
            }
            else{
                if(nums[mid] >= nums[left]){
                    left++;
                }
                else{
                    right--;
                }
            }
        }
        return nums[left];
    }
};
