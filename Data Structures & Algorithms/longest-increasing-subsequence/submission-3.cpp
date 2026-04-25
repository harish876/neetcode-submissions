class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        /*
            9   1   4   2   3   3   7
            1   1   2   2   3   1   1
                            |
        */
        int n = nums.size();
        vector<int>dp(n,1);        
        for(int i=1; i<n; i++){
            for(int j=0; j<i; j++){
                if(nums[i] > nums[j]){
                    dp[i] = max(dp[i],1+dp[j]);
                }
            }
        }
        return *max_element(dp.begin(),dp.end());
    }
};
