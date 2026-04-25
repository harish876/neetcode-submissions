class Solution {
public:
    vector<vector<int>>result;
    void dfs(vector<int>& nums,int curr,int n,vector<int>path){
        if(curr >= n){
            if(count(result.begin(),result.end(),path) == 0) result.push_back(path);
            return;
        }

        path.push_back(nums[curr]);
        dfs(nums,curr+1,n,path);
        path.pop_back();

        dfs(nums,curr+1,n,path);

    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        //all subsets backtracking and recursion
        result.clear();

        sort(nums.begin(),nums.end());
        int n = nums.size();
        dfs(nums,0,n,{});
        return result;
    }
};
