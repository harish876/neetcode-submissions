class UnionFind {
    private:
        int n;
        vector<int>parents;
    public:
        UnionFind(int _n) : n(_n) {
            parents.resize(n,0);
            for(int i=0; i<n; i++){
                parents[i] = i;
            }
        }

        int Find(int child){
            if(parents[child] == child){
                return child;
            }
            return Find(parents[child]);
        }
        
        void Union(int parent,int child){
            int p = Find(parent);
            int c = Find(child);

            if(parents[c] != p){
                parents[c] = p;
            }
        }

        int getComponents(){
            set<int>st;
            for(auto i: parents){
                st.insert(Find(i));
            }
            return st.size();
        }

        void printParents(){
            for(auto i: parents) cout<<i<<" ";
            cout<<endl;
        }

};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        //i guess union find
        //adjacency list first

        // vector<vector<int>>adj(n);
        // for(vector<int>edge: edges){
        //     int from = edge[0];
        //     int to = edge[1];

        //     adj[from].push_back(to);
        //     adj[to].push_back(from);
        // }

        // for(int i=0; i<n; i++){
        //     cout<<i<<" -> ";
        //     for(auto j:adj[i]) cout<<j<<" ";
        //     cout<<endl;
        // }

        //kruskals we might not need adj list

        UnionFind* uf = new UnionFind(n);
        for(vector<int>edge: edges){
            uf->Union(edge[0],edge[1]);
        }
        return uf->getComponents();
    }
};
