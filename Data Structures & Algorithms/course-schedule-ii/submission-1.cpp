class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& preqs) {
        vector<int>result;
        vector<vector<int>>adj(numCourses);
        vector<int>inorder(numCourses,0);

        for(vector<int>preq: preqs){
            int to = preq[0];
            int from = preq[1];

            adj[from].push_back(to);
            inorder[to]++;
        }

        queue<int>q;

        for(int i=0; i<numCourses; i++){
            if(inorder[i] == 0){
                q.push(i);
                result.push_back(i);
            }
        }

        while(!q.empty()){
            int vertex = q.front();
            q.pop();

            for(auto n: adj[vertex]){
                inorder[n]--;

                if(inorder[n] == 0) {
                    q.push(n);
                    result.push_back(n);
                }
            }
        }
        
        if(count(inorder.begin(),inorder.end(),1)){
            return {};
        }

        return result;
    }
};
