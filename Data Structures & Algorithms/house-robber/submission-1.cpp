class Solution {
public:
    vector<int>cache;
    int recurse(vector<int>&nums,int curr,int n){
        if(curr >= n){
            return 0;
        }

        if(cache[curr] != -1){
            return cache[curr];
        }

        return cache[curr] = max(
            nums[curr] + recurse(nums,curr+2,n),
            recurse(nums,curr+1,n)
        );
        
    }

    int rob(vector<int>& nums) {
        /*
            max amount of money you can rob
        */
        int n = nums.size();
        cache.resize(n+1,-1);
        return recurse(nums,0,n);
    }
};
