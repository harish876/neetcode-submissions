class Solution {
public:
    vector<vector<int>>result;
    void dfs(vector<int>& candidates, int target, int curr, int n, vector<int>path){
        if(target < 0){
            return;
        }

        if(target == 0){
            if(count(result.begin(),result.end(),path) == 0)  result.push_back(path);
            return;
        }

        if(curr >= n){
            return;
        }
        
        path.push_back(candidates[curr]);
        dfs(candidates,target-candidates[curr],curr+1,n,path);
        path.pop_back();
        
        dfs(candidates,target,curr+1,n,path);
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        result.clear();
        sort(candidates.begin(),candidates.end());
        int n = candidates.size();
        dfs(candidates,target,0,n,{});
        return result;
    }
};
