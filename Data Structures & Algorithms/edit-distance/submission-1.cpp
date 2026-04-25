class Solution {
public:
    int dfs(string w1,string w2,int i,int j){
        if(j >= w2.size()){
            return w1.size()-i;
        }

        if(i >= w1.size()){
            return w2.size() - j;
        }
        
        int cost = INT_MAX;
        if(w1[i] == w2[j]){
            cost = min(cost,dfs(w1,w2,i+1,j+1));
        }
        
        cost = min(cost,1 + dfs(w1,w2,i,j+1)); //insert
        cost = min(cost,1 + dfs(w1,w2,i+1,j+1)); //replace
        cost = min(cost,1 + dfs(w1,w2,i+1,j)); //delete

        return cost;
    }

    int minDistance(string word1, string word2) {
        /*
            m   o   n   k   e   y   s
                                |
            m   o   n   e   y
                                |
        */

        return dfs(word1,word2,0,0);
    }
};
