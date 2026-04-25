class Solution {
public:
    const vector<pair<int,int>>directions = {
        {0,1},
        {0,-1},
        {1,0},
        {-1,0}
    };


    bool isBounds(vector<vector<int>>& grid,int i,int j){
        int m = grid.size();
        int n = grid[0].size();
        return (i>=0 && j>=0 && i<m && j<n);
    }

    void dfs(vector<vector<int>>& grid,int i,int j,int acc){
        if(!isBounds(grid,i,j) || grid[i][j] != 1){
            return;
        }

        grid[i][j] = -1;
        for(pair<int,int>dir: directions){
            int x = i + dir.first;
            int y = j + dir.second;
            dfs(grid,x,y,acc+1);  
        }
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        //eez
        int m = grid.size();
        int n = grid[0].size();
        int ans = 0; //reset

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1){
                    int count = 0;
                    dfs(grid,i,j,0);
                        for(int i=0; i<m; i++){
                            for(int j=0; j<n; j++){
                                if(grid[i][j] == -1) {
                                    grid[i][j] = 2;
                                    count++;
                                }
                            }
                        }
                    ans = max(ans,count);
                }
            }
        }

        return ans;
    }
};
