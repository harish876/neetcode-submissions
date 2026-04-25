class Solution {
public:
    bool dfs(vector<vector<int>>& adj,vector<int>& visited,int curr,int parent){
        
        visited[curr] = 2; //mark it as visiting

        for(auto i: adj[curr]){
            if(i == parent) continue;

            if(visited[i] == 2){ 
                return false;
                dfs(adj,visited,i,curr);
            }

            if(visited[i] == 0){
                if(!dfs(adj,visited,i,curr)){
                    return false;
                }
            }
        }

        visited[curr] = 1; //mark it as visited

        return true;
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>>adj(n);

        for(vector<int> edge: edges){
            int from = edge[0];
            int to = edge[1];

            adj[from].push_back(to);
            adj[to].push_back(from);
        }

        vector<int>visited(n,0);
        if(!dfs(adj,visited,0,-1)){
            return false;
        }

        for (int v : visited) {
            if (v == 0) {
                return false; // Unvisited node means disconnected graph
            }
        }

        return true;
    }
};
