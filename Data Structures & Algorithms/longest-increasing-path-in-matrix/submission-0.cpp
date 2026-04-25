class Solution {
public:
    bool isBounds(vector<vector<int>>& matrix,int i,int j){
        int m = matrix.size();
        int n = matrix[0].size();

        return (i >= 0 && j >= 0 && i < m && j < n);
    }

    int result = 0;
    vector<pair<int,int>>directions = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1}
    };

    void dfs(vector<vector<int>>& matrix,int i,int j,int pathLen,vector<int>currSet){
        if(!isBounds(matrix,i,j)){

            return;
        }

        result = max(result,pathLen);
        for(auto i:currSet) cout<<i<<" "; cout<<endl;

        
        
        for(auto dir: directions){
            int newX = dir.first + i;
            int newY = dir.second + j;
            if(isBounds(matrix,newX,newY) && matrix[newX][newY] > matrix[i][j]){
                currSet.push_back(matrix[i][j]);
                dfs(matrix,newX,newY,pathLen+1,currSet);
                currSet.pop_back();
            }
        }
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                dfs(matrix,i,j,1,{});
            }
        }
        return result;
    }
};
