class Solution {
public:
    vector<int>cache;
    int recurse(vector<int>& nums,int curr,int n){
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

    int accomplice(vector<int>& nums){
        int n = nums.size();
        if(n == 1){
            return nums[0];
        }

        cache.resize(n+1,-1);
        int r1 = recurse(nums,0,n-1);
        cache.clear();
        cache.resize(n+1,-1);
        int r2 = recurse(nums,1,n);
        return max(r1,r2);

    }

    int rob(vector<int>& nums) {
        /*
            0..n-1
            1..n
        */
        return accomplice(nums);
    }
};
