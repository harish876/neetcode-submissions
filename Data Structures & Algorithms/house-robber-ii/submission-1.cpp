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

        if(n == 1){
            return nums[0];
        }

        int result1 = dfs(nums,0,n-1);
        cache.clear();
        cache.resize(n,-1);
        int result2 = dfs(nums,1,n);
        cout<<result1<<endl;
        cout<<result2<<endl;
        return max(result1,result2);
    }
};
