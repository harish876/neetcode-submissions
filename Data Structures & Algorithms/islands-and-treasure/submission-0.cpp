class Solution {
private:
    bool isValid(pair<int,int>p,int m,int n){
        int i = p.first;
        int j = p.second;
        return i>=0 && j>=0 && i<m && j<n;
    }

public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        /*
          INF  -1   0  INF
          INF  INF INF -1
          INF  -1  INF -1
          0    -1  INF INF
        */ 

        int m = grid.size();
        int n = grid[0].size();

        queue<pair<int,int>>q;
        const vector<pair<int,int>>directions = {
            {0,1},
            {0,-1},
            {1,0},
            {-1,0}
        };

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }

        while(!q.empty()){
            pair<int,int>cell = q.front();
            q.pop();

            for(pair<int,int>d: directions){
                pair<int,int>nextCell = {cell.first + d.first, cell.second + d.second};
                if(isValid(nextCell,m,n) && grid[nextCell.first][nextCell.second] == INT_MAX){
                    grid[nextCell.first][nextCell.second] = 1 + grid[cell.first][cell.second];
                    q.push(nextCell);
                } 
            }
        }
    }
};
