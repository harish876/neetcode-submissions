class Solution {
public:
    bool isBound(pair<int,int>v,int m,int n){
        return v.first >= 0 && v.second >= 0 && v.first < m && v.second < n;
    }
    void islandsAndTreasure(vector<vector<int>>& grid) {
        //idea is to think in a opposite sense
        //from the treasure i should do a BFS
        /*
        -1,0,1
         1,2,-1
        
        */
        queue<pair<int,int>>q;
        int m = grid.size();
        int n = grid[0].size();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }

        const vector<pair<int,int>>directions = {
            {1,0},
            {-1,0},
            {0,1},
            {0,-1}
        };

        while(!q.empty()){
            pair<int,int>v = q.front();
            q.pop();

            for(pair<int,int>d: directions){
                pair<int,int>neigh = {v.first + d.first, v.second + d.second};
                if(isBound(neigh,m,n) && grid[neigh.first][neigh.second] == INT_MAX){
                    grid[neigh.first][neigh.second] = 1 + grid[v.first][v.second];
                    q.push(neigh);
                }
            }
        }
    }
};
