class Solution {
public:
    vector<vector<int>>cache;
    int helper(vector<int>& prices,bool buy,int curr,int n){
        if(curr >= n){
            return 0;
        }

        if(cache[curr][buy] != -1){
            return cache[curr][buy];
        }

        int ans = 0;
        ans = max(ans,helper(prices,buy,curr+1,n)); //skip - dont do anything
        if(buy){
            ans = max(ans,helper(prices,!buy,curr+1,n) - prices[curr]); //buy
        }
        else{
            ans = max(ans,helper(prices,!buy,curr+2,n) + prices[curr]); //sell
        }

        return cache[curr][buy] = ans;
    }
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        cache.clear();
        cache.resize(n+1,vector<int>(2,-1));
        return helper(prices,true,0,n);
    }
};
