class Solution {
private:
    const vector<pair<int,int>>directions = {
        {0,1},
        {0,-1},
        {1,0},
        {-1,0}
    };

    bool isBounds(int i,int j,int m,int n){
        return (i>=0 && j>=0 && i<m && j<n);
    }

public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        //bfs
        /*
        
            3 -1   0   1
            2  2   1  -1
            1  -1  2  -1
            0  -1  3   4    
        */
        int m = grid.size();
        int n = grid[0].size();

        queue<pair<int,int>>q;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }

        while(!q.empty()){
            int sz = q.size();
            
            while(sz--){
                pair<int,int>front = q.front();
                q.pop();

                for(auto dir: directions){
                    int newX = dir.first + front.first;
                    int newY = dir.second + front.second;
                    if(isBounds(newX,newY,m,n) && grid[newX][newY] == INT_MAX){
                        grid[newX][newY] = 1 + grid[front.first][front.second];
                        q.push({newX,newY});
                    }
                }
            }
        }

    }
};
