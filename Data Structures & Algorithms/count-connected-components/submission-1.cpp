class UnionFind {
    public:
        int n;
        vector<int>parents;
        UnionFind(int _n): n(_n) {
            parents.resize(n,0);
            for(int i=0; i<n; i++){
                parents[i] = i; //each node is a parent of itself
            }
        };

        int Find(int v){
            if(parents[v] == v){
                return v;
            }
            return Find(parents[v]);
        }

        void Union(int parent,int child){
            int a = Find(parent);
            int b = Find(child);

            parents[b] = parents[a];
        }

        int getDistinctParents(){
            return set<int>(parents.begin(),parents.end()).size();
        }
};

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        /*
            0 - 1 - 2 - 3 - 4- 5

            0 1 2 3 4 5
        */
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
