class Solution {
public:
    int helper(vector<int>& nums,int target,int curr,int n){
        if(curr >= n){
            return (target == 0);
        }

        int ans = 0;
        ans += helper(nums,target-nums[curr],curr+1,n);
        ans += helper(nums,target+nums[curr],curr+1,n);
        return ans;
    }

    int findTargetSumWays(vector<int>& nums, int target) {
        int n = nums.size();
        return helper(nums,target,0,n);
    }
};
