class Solution {
public:
    vector<int>cache;
    int dfs(vector<int>&nums,int curr,int n){
        if(curr >= n){
            return 0;
        }

        if(cache[curr] != -1){
            return cache[curr];
        }

        return cache[curr] = max(
            nums[curr] + dfs(nums,curr+2,n),
            dfs(nums,curr+1,n)
        );
    }

    int rob(vector<int>& nums) {
        int n = nums.size();
        cache.resize(n,-1);
        return dfs(nums,0,n);
    }
};
