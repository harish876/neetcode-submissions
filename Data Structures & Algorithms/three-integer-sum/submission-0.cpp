class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        /*
            -4  -1  -1  0   1   2
        i        |
        l               |    
        r                       |

        -1,-1,2
        */
        sort(nums.begin(),nums.end());
        int n = nums.size();
        vector<vector<int>>result;
        for(int i=0; i<n; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int left = i+1;
            int right = n-1;

            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0){
                    result.push_back({nums[i],nums[left],nums[right]});
                    left++;
                    while(left > 0 && left < n && nums[left] == nums[left-1]){
                        left++;
                    }
                }
                else if(sum < 0){
                    left++;
                }
                else{
                    right--;
                }
            }
        }
        return result;
    }
};
