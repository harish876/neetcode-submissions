class Solution {
public:
    int BUY = 0;
    int SELL = 1;

    vector<vector<int>>cache;
    int dfs(vector<int>&prices,int curr,int prev_decision,int n){
        if(curr >= n){
            return 0;
        }

        if(cache[prev_decision][curr] != -1){
            return cache[prev_decision][curr];
        }

        int result = 0;
        int skip = dfs(prices,curr+1,prev_decision,n);
        if(prev_decision == BUY){
            int buy = max(skip,dfs(prices,curr+1,SELL,n) - prices[curr]);
            result = max(result,buy);
        }
        else{
            int sell = max(skip,dfs(prices,curr+2,BUY,n) + prices[curr]);
            result = max(result,sell);
        }

        return cache[prev_decision][curr] = result;
    }
    int maxProfit(vector<int>& prices) {
        /*
            BUY(0)
            profit = 1 
        */
        int n = prices.size();
        cache.clear();
        cache.resize(2,vector<int>(n+1,-1));
        return dfs(prices,0,BUY,n);
    }
};
