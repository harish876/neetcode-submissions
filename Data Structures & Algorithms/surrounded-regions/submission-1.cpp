std::pair<int,int> operator+(const pair<int,int>& a,const pair<int,int>& b){
    return {a.first + b.first,a.second + b.second};
}

class Solution {
public:
    const vector<pair<int,int>>directions = {
        {0,1},
        {0,-1},
        {1,0},
        {-1,0}
    };

    bool isBounds(pair<int,int>& p,int m,int n){
        return (p.first>=0 && p.second>=0 && p.first<m && p.second<n);
    }

    void solve(vector<vector<char>>& board) {
        /*
            Turn all the O's at the border to neutral
            - X X - X
            X O O X -
            X O X O X
            - X - - -
            X X - X -
        */
        int m = board.size();
        int n = board[0].size();

        queue<pair<int,int>>q;

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(i == 0 || j == 0 || i == m-1 || j == n-1){
                    if(board[i][j] == 'O'){
                        board[i][j] = '-';
                        q.push({i,j});
                    }
                }
            }
        }

        while(!q.empty()){
            pair<int,int>f = q.front();
            q.pop();

            for(auto dir: directions){
                pair<int,int>neigh = f + dir;
                if(isBounds(neigh,m,n) && board[neigh.first][neigh.second] == 'O'){
                    board[neigh.first][neigh.second] = '-';
                    q.push(neigh);
                }
            }
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == 'O') board[i][j] = 'X';
            }
        }

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(board[i][j] == '-') board[i][j] = 'O';
            }
        }


    }
};
