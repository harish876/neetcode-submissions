class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        /*
            9 1 4 2 3 3 7
            1 1 2 2 1 1 1
        */
        int n = nums.size();
        vector<int>dp(n,1);
        int result = 1;

        //O(n^2)
        for(int i=0; i<n; i++){
            for(int j=i-1; j>=0; j--){
                if(nums[i] > nums[j]){
                    dp[i] = max(dp[i],1 + dp[j]);
                }
            }
            result = max(result,dp[i]);
        }

        return result;

    }
};
