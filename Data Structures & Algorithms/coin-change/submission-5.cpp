class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        /*
            amount = 6
            coins = [1,5,10]
                0  1  2  3  4   5   6
            0   0  i  i  i  i   i   i
            1   0  1  2  3  4   5   6 
            5   0  1  2  3  4   1 
            10

        */
        int n = coins.size();
        vector<vector<int>>dp(n+1,vector<int>(amount+1,1e5));
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
        return dp[n][amount] >= 1e5 ? -1 : dp[n][amount];
    }
};
