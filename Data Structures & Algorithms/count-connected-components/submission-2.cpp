class UnionFind {
    public:
        int n;
        vector<int>parents;
        vector<int>rank;
        UnionFind(int _n): n(_n) {
            parents.resize(n,0);
            rank.resize(n,1);
            for(int i=0; i<n; i++){
                parents[i] = i; //each node is a parent of itself
            }
        };

        int Find(int v){
            if(parents[v] != v){
                parents[v] = Find(parents[v]);
            }
            return parents[v];
        }

        void Union(int parent,int child){
            int parentA = Find(parent);
            int parentB = Find(child);

            if(parentA != parentB){
                if(rank[parentA] > rank[parentB]){
                    parents[parentB] = parents[parentA];
                }
                else if(rank[parentB] > rank[parentA]){
                    parents[parentA] = parents[parentB];
                }
                else{
                    parents[parentB] = parents[parentA];
                    rank[parentA]++;
                }
            }
        }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        UnionFind *uf = new UnionFind(n);
        for(vector<int>edge : edges){
            uf->Union(edge[0],edge[1]);
        }
        set<int>s;
        for(auto i: uf->parents){
            s.insert(uf->Find(i));
        }
        cout<<endl;
        return s.size();
    }
};
