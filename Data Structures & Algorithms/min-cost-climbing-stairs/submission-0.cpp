class Solution {
public:
    vector<int>cache;
    int recurse(int curr,int n,vector<int>& cost){
        if(curr > n){
            return 0;
        }

        if(cache[curr] != -1){
            return cache[curr];
        }

        return cache[curr] = cost[curr] + min(
            recurse(curr+1,n,cost),
            recurse(curr+2,n,cost)
        );  
    }

    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        cache.resize(n,-1);
        int res1 = recurse(0,n,cost);
        cache.resize(n,-1);
        int res2 = recurse(1,n,cost);
        return min(res1,res2);

    }
};
