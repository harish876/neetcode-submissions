class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& preqs) {
        //top sort
        vector<vector<int>>adj(numCourses);
        vector<int>inorder(numCourses,0);

        for(vector<int>preq: preqs){
            int from = preq[0];
            int to = preq[1];

            adj[from].push_back(to);
            inorder[to]++;
        }

        queue<int>q;

        for(int i=0; i<numCourses; i++){
            if(inorder[i] == 0){
                q.push(i);
            }
        }

        while(!q.empty()){
            int vertex = q.front();
            q.pop();

            for(auto n: adj[vertex]){
                inorder[n]--;

                if(inorder[n] == 0) q.push(n);
            }
        }
        return count(inorder.begin(),inorder.end(),0) == numCourses;
    }
};
