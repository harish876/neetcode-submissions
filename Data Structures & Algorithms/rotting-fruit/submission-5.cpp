class Solution {
private:
    const vector<pair<int,int>>directions = {
        {0,1},
        {0,-1},
        {1,0},
        {-1,0}
    };

    bool isBounds(int i,int j,int m,int n){
        return (i >= 0 && j >= 0 && i<m && j<n);
    }

public:
    int orangesRotting(vector<vector<int>>& grid) {
        /*
            2   3   4
            0   4   5
            1   0   6
        
            bfs
        */
        int m = grid.size();
        int n = grid[0].size();
        int freshOranges = 0;
        int rottenOranges = 0;
        queue<pair<int,int>>q;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 2){
                    rottenOranges++;
                    q.push({i,j});
                }
                else if(grid[i][j] == 1){
                    freshOranges++;
                }
            }
        }

        if(freshOranges == 0){
            return 0;
        }
        else if(rottenOranges == 0){
            return -1;
        }

        int count = 0;
        while(!q.empty()){
            int sz = q.size();
            while(sz--){
                pair<int,int>front = q.front();
                q.pop();
                
                for(auto dir: directions){
                    int newX = dir.first + front.first;
                    int newY = dir.second + front.second;

                    if(isBounds(newX,newY,m,n) && grid[newX][newY] == 1){
                        grid[newX][newY] = 1 + grid[front.first][front.second];
                        q.push({newX,newY});
                    }
                }
            }
            count++;
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1){
                    return -1;
                }
            }
        }

        return count-1;


    }
};
