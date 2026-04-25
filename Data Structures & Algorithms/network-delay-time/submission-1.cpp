class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        //djkistra's??

        vector<int>distance(n+1,INT_MAX);
        vector<vector<pair<int,int>>>adj(n+1);

        for(vector<int>time: times){
            adj[time[0]].push_back({time[1],time[2]});
        }


        priority_queue<
            pair<int,int>,
            vector<pair<int,int>>,
            greater<pair<int,int>>
        >pq;

        pq.push({0,k}); //distance,vertex
        distance[k] = 0;

        while(!pq.empty()){
            pair<int,int> node = pq.top();
            pq.pop();

            for(pair<int,int> neighbor: adj[node.second]){
                //vertex and distance
                if(node.first + neighbor.second <= distance[neighbor.first]){
                    distance[neighbor.first] = node.first + neighbor.second;
                    pq.push({distance[neighbor.first],neighbor.first});
                }
            }
        }

        int result = 0;
        for(int i=1; i<=n; i++) {
            if(distance[i] == INT_MAX) return -1;
            else result = max(result,distance[i]);
        }
        return result;
    }
};
