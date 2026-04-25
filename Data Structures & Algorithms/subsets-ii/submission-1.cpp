class Solution {
public:
    vector<vector<int>>result;
    void dfs(vector<int>& nums,int curr,int n,vector<int>path){
        
        result.push_back(path);
        

        for(int i = curr; i<n; i++){
            if(i > curr && nums[i] == nums[i-1]) continue;

                path.push_back(nums[i]);

                dfs(nums,i+1,n,path);

                path.pop_back();
        }

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
