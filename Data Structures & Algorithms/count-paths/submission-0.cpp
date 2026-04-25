class Solution {
public:
    bool isBounds(vector<vector<int>>& grid,int i,int j){
        int m = grid.size();
        int n = grid[0].size();

        return (i >= 0 && j >= 0 && i < m && j < n);
    }

    vector<vector<int>>cache;
    int helper(vector<vector<int>>& grid,int i,int j){
        if(!isBounds(grid,i,j) || grid[i][j] == 1){
            return 0;
        }

        if(i == grid.size()-1 && j == grid[0].size()-1){
            return 1;
        }

        if(cache[i][j] != -1){
            return cache[i][j];
        }

        int ans = 0;

        grid[i][j] = 1;
        ans += helper(grid,i+1,j); //down
        ans += helper(grid,i,j+1); //right
        grid[i][j] = 0;

        return cache[i][j] = ans;
    }

    int uniquePaths(int m, int n) {
        /* probably caching here*/
        vector<vector<int>>grid(m,vector<int>(n,0));
        cache.clear();
        cache.resize(m+1,vector<int>(n+1,-1));
        return helper(grid,0,0);

    }
};
