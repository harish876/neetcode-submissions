class DSU {
    private:
        int n;
        vector<int>parents;
        vector<int>rank;
    
    public:
        DSU(int _n): n(_n) {
            parents.resize(n+1,0);
            rank.resize(n+1,1);
            for(int i=1; i<=n; i++){
                parents[i] = i;
            }
        }

        int Find(int child){
            if(parents[child] != child){
                parents[child] = Find(parents[child]);
            }
            return parents[child];
        }

        bool Union(int parent,int child){
            int p1 = Find(parent);
            int p2 = Find(child);

            if(p1 == p2){
                return false;
            }
            else if(rank[p1] > rank[p2]){
                parents[p2] = p1;
                rank[p1] += rank[p2];
            }
            else{
                parents[p1] = p2;
                rank[p2] += rank[p1];
            }
            return true;
        }

};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        DSU ds(edges.size());
        for(vector<int>edge: edges){
            int from = edge[0];
            int to = edge[1];
            if(!ds.Union(from,to)){
                return {from,to};
            }
        }
        return {};
    }
};
