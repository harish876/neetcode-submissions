class Solution {
private:
    bool isValid(pair<int,int>p,int m,int n){
        int i = p.first;
        int j = p.second;
        return i>=0 && j>=0 && i<m && j<n;
    }
public:
    int orangesRotting(vector<vector<int>>& grid) {
        /*
        level bfs()

            2 2 2
            0 1 1
            1 0 1

            [(2,2)]
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

        int rottenOranges = 0;
        int freshOranges = 0;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 2) {
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

        
        int result = 0;
        while(!q.empty()){
            int sz = q.size();
            while(sz--){
                pair<int,int>cell = q.front();
                q.pop();

                for(pair<int,int>d : directions){
                    pair<int,int>nextCell = {cell.first + d.first,cell.second + d.second};
                    if(isValid(nextCell,m,n) && grid[nextCell.first][nextCell.second] == 1){
                        grid[nextCell.first][nextCell.second] = 2;
                        q.push(nextCell);
                    }
                }
            }
            result+=1;
        }
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 1){
                    return -1;
                }
            }
        }
        return result-1;
    }
};