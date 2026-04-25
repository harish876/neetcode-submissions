class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for(int num:nums){
            sum+=num;
        }
        if(sum % 2 == 1){
            return false;
        }
        int target = sum/2;
        vector<vector<int>>dp(n+1,vector<int>(target+1,false));
        dp[0][0] = true;

        for(int i=1; i<=n; i++){
            for(int j=0; j<=target; j++){
                if(j < nums[i-1]){
                    dp[i][j] = dp[i-1][j];
                }
                else{
                    dp[i][j] = dp[i-1][j] || dp[i-1][j - nums[i-1]];
                }
            }
        }
        return dp[n][target];
    }
};
