class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        int MAX = 1e5;
        vector<vector<int>>dp(n+1,vector<int>(amount+1,MAX));
        dp[0][0] = 0;

        for(int i=1; i<=n; i++){
            for(int j=0; j<=amount; j++){
                if(j >= coins[i-1]){
                    dp[i][j] = min(dp[i-1][j],1 + dp[i][j - coins[i-1]]);
                }
                else{
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[n][amount] >= MAX ? -1 : dp[n][amount];
    }
};
